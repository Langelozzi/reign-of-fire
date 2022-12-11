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

        The character and enemy dictionaries do get modified during execution.

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

            self.__current_hp -= round(damage_given)

            Helpers.print_in_color(f"But the {self.__name}'s attack lands successfully as well", "cyan")
            # character health with decrease by 10 * (1 + (0.2 * enemy level))
            damage_taken = 10 * (1 + (0.2 * self.__level))

            updated_hp = round(character.get_current_hp() - damage_taken)
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

            if enemy_item and (enemy_item["type"] == "staff") and (
                    enemy_item["rarity"] > character.get_staff()["rarity"]):
                staff = {
                    key: value for key, value in enemy_item.items() if key != 'type'
                }
                character.set_staff(staff)

                Helpers.print_in_color(
                    f"[{character.get_name()} | {enemy_item['type']}: +{enemy_item['name']}]\n",
                    "yellow")
            elif (
                    enemy_item and
                    enemy_item["type"] == "armour" and
                    enemy_item["rarity"] > character.get_armour()["rarity"]
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
