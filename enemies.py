"""
Module contains Enemy class.
"""

from helpers import Helpers


class Enemy:
    """
    A class to represent an enemy in the game.
    """

    def __init__(self, enemy_data: dict):
        if type(enemy_data) is not dict:
            raise TypeError("Enemy_data must be a dictionary")

        self.__name = enemy_data["name"]
        self.__max_hp = enemy_data["max_hp"]
        self.__current_hp = enemy_data["current_hp"]
        self.__level = enemy_data["level"]
        self.__item = enemy_data["item"]

    def fight(self, character) -> bool:
        """
        Print dialog and receive decisions for battle mechanics.

        :param character: a Character object
        :precondition: character must be a Character object
        :postcondition: prints dialog and receives decisions for battle mechanics
        :postcondition: returns True if character wins the fight, otherwise False
        :return: True if character wins the fight, otherwise False
        """
        Helpers.print_in_color(f"\nBoth you and the {self.__name} step forward, and prepare for a battle..\n", "cyan")

        while (character.get_current_hp() > 0) and (self.__current_hp > 0):
            ability_options = list(enumerate(character.get_abilities(), start=1))
            Helpers.print_user_options(ability_options, "Ability")

            chosen_ability = Helpers.get_user_choice(ability_options)

            Helpers.print_in_color(f"\nYour {chosen_ability} hits the {self.__name}", "cyan")
            # enemy health will decrease by character damage * character level * (1 + (0.1 * staff rarity))
            try:
                damage_given = (character.get_damage() * character.get_level() *
                                (1 + (0.2 * character.get_staff()["rarity"])))
            except TypeError:
                damage_given = character.get_damage() * character.get_level()

            if (self.__current_hp - round(damage_given)) < 0:
                self.__current_hp = 0
            else:
                self.__current_hp -= round(damage_given)

            Helpers.print_in_color(f"But the {self.__name}'s attack lands successfully as well", "cyan")
            # character health with decrease by 10 * (1 + (0.2 * enemy level))
            damage_taken = 10 * (1 + (0.2 * self.__level))

            updated_hp = round(character.get_current_hp() - damage_taken)
            if updated_hp < 0:
                updated_hp = 0
            character.set_current_hp(updated_hp)

            Helpers.print_in_color(
                f"\n[{character.get_name()} | hp: {character.get_current_hp()}/{character.get_max_hp()}]", "yellow"
            )
            print(f"[{self.__name} | hp: {self.__current_hp}/{self.__max_hp}]")

        if (self.__current_hp <= 0) and (character.get_current_hp() > 0):
            Helpers.print_in_color(f"\n\nCongratulations! You have defeated the {self.__name}", "cyan")

            if self.__level > character.get_level():
                earned_xp = 15 * ((self.__level - character.get_level()) + 1)
            else:
                earned_xp = 15

            if character.get_level() < 3:
                updated_xp = round(character.get_xp() + earned_xp)
                character.set_xp(updated_xp)
                Helpers.print_in_color(f"\n[{character.get_name()} | xp: +{earned_xp}]", "yellow")

            enemy_item = self.__item

            try:
                character_staff_rarity = character.get_staff()["rarity"]
            except TypeError:
                character_staff_rarity = 0

            try:
                character_armour_rarity = character.get_armour()["rarity"]
            except TypeError:
                character_armour_rarity = 0

            if (
                    enemy_item and
                    enemy_item["type"] == "staff" and
                    enemy_item["rarity"] > character_staff_rarity
            ):
                staff = {
                    key: value for key, value in enemy_item.items() if key != 'type'
                }
                character.set_staff(staff)

                Helpers.print_in_color(
                    f"[{character.get_name()} | {enemy_item['type']}: +{enemy_item['name']}]\n", "yellow"
                )
            elif (
                    enemy_item and
                    enemy_item["type"] == "armour" and
                    enemy_item["rarity"] > character_armour_rarity
            ):
                armour = {
                    key: value for key, value in enemy_item.items() if key != 'type'
                }
                character.set_armour(armour)

                Helpers.print_in_color(
                    f"[{character.get_name()} | {enemy_item['type']}: +{enemy_item['name']}]\n",
                    "yellow")

            self.__current_hp = self.__max_hp
            return True

        self.__current_hp = self.__max_hp
        return False

    def battle(self, character) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start an enemy battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start an enemy battle
        :postcondition: returns True if character wins the enemy battle, otherwise False
        :return: True if character wins the enemy battle, otherwise False
        """
        Helpers.print_in_color(f"Out of the corner of your eye you see a {self.__name} appear!\n", "cyan")

        if character.get_level() < self.__level:
            Helpers.print_in_color(f"This enemies level is greater than yours, you might want to weigh your options "
                                   f"before "
                                   f"you make your decision\n", "red")

        options = list(enumerate(["Fight", "Flee"], start=1))

        Helpers.print_user_options(options, "Choice")

        decision = Helpers.get_user_choice(options, True)

        if int(decision) == 1:
            return self.fight(character)
        else:
            Helpers.print_in_color(f"\nAs you turn to flee the {self.__name} says:", "cyan")
            print("I should have guessed. You do seem like a cowardly creature. I will be here if you wish "
                  "to return with a bit more courage..")
            return False


class RoyalMageAngelozzi(Enemy):
    def __init__(self):
        angelozzi = {
            "name": "Royal Battle-Mage Angelozzi",
            "max_hp": 250,
            "current_hp": 250,
            "level": 7,
            "item": {
                "type": "staff",
                "name": "Angelozzi's Ill-Omen",
                "rarity": 5
            }
        }

        super().__init__(angelozzi)

    def battle(self, character) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the mini boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the mini boss battle
        :postcondition: returns True if character wins the mini boss battle, otherwise False
        :return: True if character wins the mini boss battle, otherwise False
        """
        Helpers.print_in_color("As you exit the narrow collider, you arrive at a grand opening to what seems like a "
                               "giant "
                               "underground cave...You notice a cathedral in the distance.\n\n"
                               "'How can someone build something so magnificent underground,' you thought.\n", "cyan")
        Helpers.print_in_color("As you stand there in awe, you notice a huge knight clad in royal armour towering over "
                               "the "
                               "cathedral entrance.\n", "cyan")
        Helpers.print_in_color(f"You approach the giant knight to observe them better.\n", "cyan")

        if character.get_level() <= 3:
            Helpers.print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options "
                                   f"before "
                                   f"you make your decision\n", "red")

        options = list(enumerate(["Fight", "Flee"], start=1))
        Helpers.print_user_options(options, "Choice")

        decision = Helpers.get_user_choice(options, True)

        if int(decision) == 1:
            Helpers.print_in_color(f"The battle mage notices you, he readies his staff: \n", "cyan")
            print("You wretched createre, how dare you stain this sacred haven with your miserable existence.\n"
                  "Instead of fulfilling your duty as one of the royal knights, you chose to betray our King.\n"
                  "I do not know how you escaped your cell, but on my honour as the Left wing of Alyndelle, "
                  "the guardian of this empire, I must stop you.\n")

            return super().fight(character)
        else:
            Helpers.print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False


class LordCommanderYmir(Enemy):
    def __init__(self):
        ymir = {
            "name": "Lord-Commander Ymir",
            "max_hp": 400,
            "current_hp": 400,
            "level": 5,
            "item": {
                "type": "armour",
                "name": "Ymir's Royal Armour",
                "rarity": 5
            }
        }

        super().__init__(ymir)

    def battle(self, character) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the mini boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the mini boss battle
        :postcondition: returns True if character wins the mini boss battle, otherwise False
        :return: True if character wins the mini boss battle, otherwise False
        """
        Helpers.print_in_color("You reach closer to the throne room, and arrive at a grand hall supported by marble "
                               "pillars \n"
                               "and the statues depict the past heroes and kings of Alyndelle.\n",
                               "cyan")
        Helpers.print_in_color("***CRASH***.\n"
                               "There's dust and smoke everywhere!\n"
                               "*cough cough*\n"
                               "You see a huge figure appear as the dust settles.", "cyan")
        Helpers.print_in_color("He is clad in ornate armor; those scratches and gouges on his armor proving the "
                               "warrior's "
                               "skill.\n", "cyan")

        if character.get_level() <= 3:
            Helpers.print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options "
                                   f"before "
                                   f"you make your decision\n", "red")

        options = list(enumerate(["Fight", "Flee"], start=1))
        Helpers.print_user_options(options, "Choice")

        decision = Helpers.get_user_choice(options, True)

        if int(decision) == 1:
            Helpers.print_in_color(f"The giant knight notices you, and he readies his greatsword: \n", "cyan")
            print("I commend you for making this far, but, your luck ends here, mortal.\n"
                  "On my honour as the Right wing of Alyndelle, the guardian of this empire,\n"
                  "and as the Lord-Commander, I must stop you.\n")

            return super().fight(character)
        else:
            Helpers.print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False


class GodKingThompson(Enemy):
    def __init__(self):
        thompson = {
            "name": "God-King Thompson",
            "max_hp": 450,
            "current_hp": 450,
            "level": 6,
            "item": {
                "type": "staff",
                "name": "Demonic Python Staff",
                "rarity": 7
            }
        }

        super().__init__(thompson)

    def battle(self, character) -> bool:
        """
        Print dialog and receive decisions for choosing whether to start the final boss battle.

        The character dictionary is modified during execution.

        :param character: a character in dictionary form
        :precondition: character must be a dictionary in the form of our game character with all proper keys
        :postcondition: prints dialog and receive decisions for choosing whether to start the final boss battle
        :postcondition: returns True if character wins the final boss battle, otherwise False
        :return: True if character wins the final boss battle, otherwise False
        """
        Helpers.print_in_color("As you enter into throne room, you see a colossal of a man sitting on the Golden "
                               "throne.\n"
                               "He must be the king, the man who stole the light and betrayed the very gods itself.\n",
                               "cyan")
        Helpers.print_in_color("You approach the golden throne\n", "cyan")

        if character.get_level() <= 3:  # max level is three?
            Helpers.print_in_color(f"\nThis enemies level is greater than yours, you might want to weigh your options "
                                   f"before "
                                   f"you make your decision\n", "red")

        options = list(enumerate(["Fight", "Flee"], start=1))
        Helpers.print_user_options(options, "Choice")

        decision = Helpers.get_user_choice(options, True)

        if int(decision) == 1:
            Helpers.print_in_color("The King acknowledge you, and readies his Warhammer: \n", "cyan")
            print("You have done well, mortal. It is commendable. However, as the God King of Alyndelle,"
                  "I cannot allow your transgression no longer.\nYour treachery will end here, I will not "
                  "allow the Flame of Humanity to be restored. This is the sacrifice your kind must make "
                  "for my victory.")

            return super().fight(character)
        else:
            Helpers.print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False
