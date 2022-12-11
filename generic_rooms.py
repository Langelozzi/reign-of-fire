"""
Module contains GenericRooms class.
"""

from helpers import Helpers


class GenericRooms:
    """
    A class containing generic room methods.
    """

    @staticmethod
    def spider_web_blockade(character) -> None:
        """
        Print the spider web blockade room dialog and interactions.

        :param character: a Character object
        :precondition: character must be a Character object
        :postcondition: prints the spider web blockage room description dialog and interactions
        """
        Helpers.print_in_color(
            "You pause once in the room. You see that all of the archways are blocked off with layers "
            "upon \n"
            "layers of spider webs. You need some way to clear the archways before you can proceed.",
            "cyan")
        Helpers.print_in_color("You might be able to use one of your abilities to clear the webs!\n", "cyan")

        ability_options = list(enumerate(character.get_abilities(), start=1))
        Helpers.print_user_options(ability_options, "Ability")

        ability_used = Helpers.get_user_choice(ability_options)
        while ability_used != "Fireball":
            Helpers.print_in_color(f"\nI don't think {ability_used} will work here, try a different one.", "red")
            ability_used = Helpers.get_user_choice(ability_options)

        Helpers.print_in_color("\n\nNice work! You were able to clear out all of those webs with your Fireball!",
                               "cyan")

        if character.get_level() < 3:
            new_xp = character.get_xp() + 12
            character.set_xp(new_xp)

            Helpers.print_in_color(f"\n[{character.get_name()} | xp: +12]", "yellow")

    @staticmethod
    def empty_room(character) -> bool:
        """
        Print the empty room dialog with the character name.

        :param character: a Character object
        :precondition: character must be a Character object
        :postcondition: prints the empty room dialog with the character name
        """
        Helpers.print_in_color(
            "You stop in the center of the room. It appears empty, but you hear a voice whispering..",
            "cyan")
        Helpers.print_in_color(f"{character.get_name()}, keep walking if you know what's good for you!", "cyan")
        Helpers.print_in_color("You hastily make your decision..", "cyan")

        return True
