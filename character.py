"""
Contains functions related to the game characters attributes and state.
"""

from helpers import Helpers


class Character:
    def __init__(self, name: str) -> None:
        """
        Instantiate a new character object with name.

        :param name: the name of the character, as a string
        :precondition: name must be a string
        :postcondition: instantiates a new character object with name
        """
        if type(name) != str:
            raise TypeError('Character name must be a string!')

        self.__name = name
        self.__position = (1, 1)
        self.__max_hp = 100
        self.__current_hp = 100
        self.__xp = 0
        self.__damage = 20
        self.__level = 1
        self.__abilities = ["Fireball"]
        self.__staff = None
        self.__armour = None

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_max_hp(self):
        return self.__max_hp

    def get_current_hp(self):
        return self.__current_hp

    def set_current_hp(self, hp: int):
        if type(hp) is not int:
            raise TypeError('hp must be an integer')
        if (hp < 0) or (hp > self.__max_hp):
            raise ValueError('hp must be between 0 and 60 inclusive')

        self.__current_hp = hp

    def get_xp(self):
        return self.__xp

    def set_xp(self, xp: int):
        if type(xp) is not int:
            raise TypeError('xp must be an integer')
        if (xp < 0) or (xp > 60):
            raise ValueError('xp must be between 0 and 60 inclusive')

        self.__xp = xp

    def get_damage(self):
        return self.__damage

    def get_level(self):
        return self.__level

    def get_abilities(self):
        return self.__abilities

    def get_staff(self):
        return self.__staff

    def set_staff(self, new_staff: dict):
        if type(new_staff) is not dict:
            raise TypeError("Staff must be a dictionary")

        self.__staff = new_staff

    def get_armour(self):
        return self.__armour

    def set_armour(self, new_armour: dict):
        if type(new_armour) is not dict:
            raise TypeError("Armour must be a dictionary")

        self.__staff = new_armour

    def add_ability(self, new_ability: str) -> None:
        self.__abilities.append(new_ability)

    def show_stats(self) -> None:
        """
        Print the character's statistics formatted to stdout.

        :postcondition: prints the character's statistics formatted to stdout
        """
        print('+----------------------------------------------------------------------------------+')
        print('|', end="")
        Helpers.print_in_color('{:^82}'.format(self.__name), "red", end="")
        print('|')
        print('+----------------------------------------------------------------------------------+')

        general_stats = [
            ("Current Coordinates", self.__position),
            ("Level", self.__level),
            ("HP", f"{round(self.__current_hp)}/{self.__max_hp}"),
        ]
        xp_stat = ("XP (to next level)", f"{round(self.__xp)}/60") if self.__level < 3 \
            else ("XP (to next level)", "Max")

        general_stats.append(xp_stat)

        for title, stat in general_stats:
            print('{:<18}'.format("|"), end="")
            Helpers.print_in_color(f"{title:<20}", "blue", end="")
            print("{:<45}".format(f": [ {stat} ]"), end="")
            print('|')

        print('+----------------------------------------------------------------------------------+')

        inventory_stats = (
            ("Staff", self.__staff),
            ("Armour", self.__armour)
        )
        for item, gear in inventory_stats:
            print('{:<18}'.format("|"), end="")
            Helpers.print_in_color(f"{item:<20}", "blue", end="")
            try:
                print('{:<54}'.format(
                    f": [ {gear['name']} (\033[93m{'*' * gear['rarity']}\033[0m) ]"),
                    end="")
            except TypeError:
                print('{:<45}'.format(f": None"), end="")
            print('|')

        print('+----------------------------------------------------------------------------------+')

        print('{:<18}'.format("|"), end="")
        Helpers.print_in_color("{:<20}".format("Abilities"), "blue", end="")
        print("{:<45}".format(f": [ {self.__abilities[0]} ]"), end="")
        print('|')

        for ability in self.__abilities[1:]:
            print('{:<38}'.format("|"), end="")
            print("{:<45}".format(f"  [ {ability} ]"), end="")
            print('|')

        print('+----------------------------------------------------------------------------------+')

    def choose_direction(self, board) -> str:
        """
        Print possible choices and return the user's selected choice.

        The board and character dictionaries are not modified.

        :param board: a board object
        :precondition: board must be a board object
        :postcondition: prints the possible choices and returns the user selected choice as a string
        :return: the user selected choice as a string
        """
        current_room = board.get_board()[self.__position]
        possible_directions = [direction for direction, coord in current_room["directions"].items() if
                               coord is not None]

        options = [('q', "quit"), ('s', "show stats")]
        options += list(enumerate(possible_directions, start=1))

        Helpers.print_user_options(options, "Option")

        return Helpers.get_user_choice(options)

    def move(self, direction: str, board) -> None:
        """
        Modify the character position accordingly based on the direction. Original character is modified, board is not.

        :param direction: one of the following strings in lowercase: "north", "east", "south", "west"
        :param board: an instance of the Board class
        :precondition: direction must be one of the following strings in lowercase: "north", "east", "south", "west"
        :precondition: board must be a Board object
        :postcondition: changes the character position according to the direction they moved
        """
        current_room = board.get_board()[self.__position]
        self.__position = current_room["directions"][direction]

    def is_alive(self) -> bool:
        """
        Determine if the character is still alive or not. Does not modify the character dictionary.

        :postcondition: Returns True if character is alive, False otherwise
        :return: True if character is alive, False otherwise
        """
        if self.__current_hp <= 0:
            return False
        else:
            return True

    def leveled_up(self) -> bool:
        """
        Determine if the character has leveled up. Does not modify the character dictionary.

        :postcondition: returns True if the character leveled up, otherwise False
        :return: True if the character leveled up, otherwise False
        """
        return True if (self.__xp >= 60) and (self.__level < 3) else False

    def level_up_sequence(self) -> None:
        """
        Increase character level, reset xp to 0 and print ascii art. Modifies the original character dictionary.

        :postcondition: increases the character level, resets xp to 0 and prints ascii art.
        """
        self.__level += 1
        self.__xp = 0
        Helpers.print_in_color("""
                              _                              _     _    _           _                                                             
                             | |                            | |   | |  | |         | |                                                            
                             | |        ___  __   __   ___  | |   | |  | |  _ __   | |                                                            
                             | |       / _ \ \ \ / /  / _ \ | |   | |  | | | '_ \  | |                                      
                             | |____  |  __/  \ V /  |  __/ | |   | |__| | | |_) | |_|                                      
                             |______|  \___|   \_/    \___| |_|    \____/  | .__/  (_)                                      
                                                                           | |                                                                    
                                                                           |_|                                                                    
                                         \U0001F386 Congrats you leveled up \U0001F386 	                
        """, "yellow")
        Helpers.print_in_color("You feel stronger, your veins are coursing with denser magic and your mana shield has "
                               "strengthened!", "yellow")

    def died(self) -> None:
        """
        Resets character position to start and character level to 1 as if they just started the game.

        All items and abilities are retained. Ascii art gets printed. Modifies the original character dictionary.

        :postcondition: Resets character position to start and character level to 1
        """
        self.__position = (1, 1)
        self.__xp = 0
        self.__level = 1
        self.__current_hp = 100

        Helpers.print_in_color("""
                             __     __                    _____    _              _                                     
                             \ \   / /                   |  __ \  (_)            | |                                    
                              \ \_/ /    ___    _   _    | |  | |  _    ___    __| |                                    
                               \   /    / _ \  | | | |   | |  | | | |  / _ \  / _` |                                    
                                | |    | (_) | | |_| |   | |__| | | | |  __/ | (_| |                                    
                                |_|     \___/   \__,_|   |_____/  |_|  \___|  \__,_|                                    
                                          \U00002620 Rip, you died. Skill issue. \U00002620                                                  
        """, "red")


def main() -> None:
    """
    Drive the program.
    """
    print("You are attempting to execute the character.py module.")
    print("Executing this module does not do anything.")


if __name__ == "__main__":
    main()
