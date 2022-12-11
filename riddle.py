"""
Contains the Riddle class.
"""

import time
from helpers import Helpers


class Riddle:
    """
    Class to represent a single riddle.
    """

    def __init__(self, riddle_data: dict):
        if type(riddle_data) is not dict:
            raise TypeError("Riddle data must be a dictionary")

        self.__question = riddle_data["question"]
        self.__options = riddle_data["options"]
        self.__answer = riddle_data["answer"]
        self.__ability = riddle_data["ability"]

    def riddle_success(self, character) -> None:
        """
        Print dialog and accept input for decisions after correctly answering a riddle.

        :param character: a Character object
        :precondition: character must be a Character object
        :postcondition: prints dialog and accepts input for decisions after correctly answering a riddle
        """
        Helpers.print_in_color(f"\n\nCongratulations {character.get_name()}, you are not as dumb as I thought for a "
                               f"creature "
                               f"such "
                               f"as yourself.", "green")

        if character.get_level() < 3:
            updated_xp = round(character.get_xp() + 15)
            character.set_xp(updated_xp)

            Helpers.print_in_color(f"\n[{character.get_name()} | xp: +15]", "yellow")

        Helpers.print_in_color(f"\n\nTo reward your success, I give you two options: try your luck at possibly "
                               f"earning a "
                               f"new ability, or accept the gift of maximum health", "green")

        success_options = list(enumerate(["Try my luck at a new ability", "Refill HP to max"], start=1))

        Helpers.print_user_options(success_options, "Choice")

        user_choice = Helpers.get_user_choice(success_options, True)

        if int(user_choice) == 1:
            new_ability = self.__ability
            if (
                    new_ability is not None and
                    new_ability not in character.get_abilities()
            ):
                character.add_ability(new_ability)
                print(f"\nYou got lucky! I am feeling generous and will grant you a new ability. You can now use "
                      f"{new_ability}")
                Helpers.print_in_color(f"\n[{character.get_name()} | abilities: +'{new_ability}']", "yellow")
            else:
                print("\nOh no, looks like you lost the coin flip, you will not be getting a new ability.")
        else:
            difference = character.get_max_hp() - character.get_current_hp()
            character.set_current_hp(character.get_max_hp())
            Helpers.print_in_color(f"\n[{character.get_name()} | hp: +{difference}]", "yellow")

    def tell(self, character) -> bool:
        """
        Print dialog and accept input for answering a riddle.

        :param character: a Character object
        :precondition: character must be a Character object
        :postcondition: prints dialog and accepts input for answering a riddle
        """
        Helpers.print_in_color("As you enter a dark, candle-lit room; you notice a mysterious potion placed by your "
                               "feet.\n"
                               "You picked it up out of curiosity, but it started to shake violently.", "cyan")
        Helpers.print_in_color("***POOF***", "cyan")
        Helpers.print_in_color("Through the thick purple smoke, a Phantom Imp appears, with unnaturally wide smile, \n"
                               "and in a high-pitch crackle, speaks:", "cyan")
        time.sleep(3)

        Helpers.print_in_color(r"""
                        _.----._     _.---.
                     .-'        `-.-'      `.
                   .'                 .:''':.`.
                 .'        .:'''':. .' .----.  `.
             .-./        .' .----.    /  .-. \   `.
            /.-.           /  .-. \   \ ' O ' |    \
            ||        `.   | ' O '/    \ `-' /     |
            || (        \   \ `-'/      `-.__     / `.
             \`-'        )   .-'  --         )        `.
              `-'     _.'   (            _.-'    _/\    \
                 `.       /\_ `-.____..-'     .-' _/    /
                   `.     \_ `-._         _.-'_.-'   .' 
                     `--.._ `-._ `-.__..-'_.-'     .' 
                   .-'     `-._ `--.__..-'  _.----'`. 
                  /            `---.......-' _     \ \ 
                 /                          ( `-._.-` )
                /  /     _                  .-    _.-' 
               (  `-._.-' )                (_   .'    \ 
                `-._      -.               (_.-'       |
                    `.     _)                   __..---'
                   |  `-._) ''...__ .-. __...'''__..---'
                    \      '''...__((=))__...'''      /
                     |              `-'             .'
                     \                             /
                      |                           |
                      \     \    \      /    /   /
                       `. \               /     /
                         `.    \   \   /   /   /
                           `--.._   ` '  _.--'
                                  [====]
                                   )  (
                                .-'    '-.
                               |          |
                               | .------. |
                               | | LGBT | |
                               | '------' |
                               |          |
                               '----------'
                               """, "green")

        print(f"Oh {character.get_name()}, you foolish creature, how dare you interrupt my slumber. For your "
              f"transgression you must prove your intellect to me with a riddle if you want me to spare your life..\n")
        time.sleep(1)
        Helpers.print_in_color(self.__question, "purple")

        options = list(enumerate(self.__options, start=1))

        Helpers.print_user_options(options, "Response")

        Helpers.print_in_color("\nYou have one chance to guess the answer or you will be punished.\nPlease choose the "
                               "correct "
                               "answer to this riddle..", "purple")

        user_answer = Helpers.get_user_choice(options)

        if user_answer == self.__answer:
            self.riddle_success(character)
            return True
        else:
            Helpers.print_in_color(f"\n{character.get_name()}, I knew a creature such as yourself was not "
                                   f"intellectually gifted. That answer is far from correct and for that you must be "
                                   f"punished!", "red")

            lost_hp = character.get_current_hp() * 0.25
            updated_hp = round(character.get_current_hp() - lost_hp)

            character.set_current_hp(updated_hp)

            Helpers.print_in_color(f"\n[{character.get_name()} | hp: -{lost_hp}]", "yellow")

            return False


def main() -> None:
    """
    Drive the program.
    """
    print("You are attempting to execute the riddle.py module.")
    print("Executing this module does not do anything.")


if __name__ == "__main__":
    main()
