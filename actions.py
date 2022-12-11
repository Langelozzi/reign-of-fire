"""
Contains functions related to the actions and dialog of each room on the game board.
"""
import itertools
import random
import json

from character import Character
from helpers import Helpers
from riddle import Riddle
from generic_rooms import GenericRooms
from enemies import Enemy


# Final Boss: God-King Thompson ----------------------------------------------------------------------------------------
def god_king_thompson():
    """
    Generate and return the god king thompson final boss battle function.

    :postcondition: generates and returns the god king thompson final boss battle function
    :return: the god king thompson final boss battle function
    """
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

    def thompson_battle(character: Character) -> bool:
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

        decision = fight_decision()

        if int(decision) == 1:
            Helpers.print_in_color("The King acknowledge you, and readies his Warhammer: \n", "cyan")
            print("You have done well, mortal. It is commendable. However, as the God King of Alyndelle,"
                  "I cannot allow your transgression no longer.\nYour treachery will end here, I will not "
                  "allow the Flame of Humanity to be restored. This is the sacrifice your kind must make "
                  "for my victory.")

            return fight(character, thompson)
        else:
            Helpers.print_in_color(f"\nYou fled. You should probably get stronger first.", "cyan")
            return False

    return thompson_battle


def create_batch_of_enemy_battles(amount: int) -> list:
    """
    Read a list of json data and generate a list of length amount, containing battle functions generated from json data.

    :param amount: an integer greater than 0
    :precondition: amount must be an integer greater than 0
    :postcondition: generates a list of length amount, containing battle functions generated from json data
    :return: a list of length amount, containing battle functions generated from json data
    """
    battles = []

    with open("json/enemies.json") as file_object:
        enemy_data = json.load(file_object)

        for enemy in enemy_data:
            new_enemy = Enemy(enemy)
            battles.append(new_enemy.battle)

    return battles[:amount + 1]


def create_batch_of_riddles(amount: int) -> list:
    """
    Read a list of json data and generate a list of length amount, containing riddle functions generated from json data.

    :param amount: an integer greater than 0
    :precondition: amount must be an integer greater than 0
    :postcondition: generates a list of length amount, containing riddle functions generated from json data
    :return: a list of length amount, containing riddle functions generated from json data
    """
    riddles = []

    with open("json/riddles.json") as file_object:
        riddles_data = json.load(file_object)

        for riddle in riddles_data:
            new_riddle = Riddle(riddle)
            riddles.append(new_riddle.tell)

    return riddles[:amount + 1]


def get_generic_room_description() -> str:
    """
    Return a random room description selected from a list.

    :postcondition: selects and returns a random room description as a string
    :return: a random room description as a string
    """
    descriptions = [
        "\nAs your foot passes the threshold into the next room, you feel something slither across your toes..",
        "\nYou are approaching the next room, and you see a dark mist fly past the archway..",
        "\nThe room feels cold and appears empty, but you sense a presence lingering..",
        "\nYou can taste the dampness in the air as you enter through the arched cobblestone..",
        "\nThe cold stone walls seem to radiate brisk air as you enter the room..",
        "\nYou step forward into the next room, you examine the walls and notice the hand of a skeleton jammed between "
        "two stones..",
        "\nYou hear the soft tapping of spider legs across the cobblestone archway..",
        "\nBeyond the cobblestone archway is a crumbling room, covered in crawling insects, broken pottery and bat "
        "droppings..",
        "\nTo the west you see a small statue of the queen's crown, crumbling onto the stone floor. It is covered in "
        "small bones, rat droppings and dead insects..",
        "\nA warn banner hangs from archway, displaying the crest of our dear queen. It is battered and torn, "
        "covered in condensation and insects..",
        "\nA fallen statue blocks the archway. You are able to slip through under arm, and enter into a room too "
        "clean for comfort..",
        "\nYou hear the drip of water to your east. There is a small fountain streaming out of the mouth of a stone "
        "gargoyle, mounted to the wall..",
        "\nA dim torch highlights the features of a pillaged statue, that has been eaten by time itself..",
        "\nThe deep purple banners flood the walls, with bats gripping to the bottom. You enter silently as to not "
        "disrupt them..",
        "\nA small puddle makes contact with the sole of your foot. You look up to see a crack in the cobblestone "
        "dripping at an unsettling-ly slow pace..",
        "\nIvy cracks the cobblestone and lines the ceiling. It's vines seem to plague the room, having propagated "
        "from north wall..",
        "\nA gloomy torch sits on the wall to the south. It's light fading with each grain of the hourglass..",
        "\nUnder your foot you hear the crack of bone. The room is a wasteland of bone and insects..",
        "\nA minor hum echoes off of the cobblestone walls. It is not random, but in an unsettling rhythm..",
        "\nA grand statue of the kingdom stands 10 feet tall in the far corner of the room, silently inspiring you to "
        "escape..",
        "\nOvergrown vines plague the stone floor, making you conscious of your feet. You fear that getting your foot "
        "stuck could render you a target for attack..",
        "\nBroken pottery carpets the floor. As you step you hear the cracking and fear that there may be creatures "
        "lurking beneath..",
        "\nYou advance carefully deeper through the castle dungeon, and enter a dark room, lit only by a dim torch..",
        "\nThe archway to the next room is crumbling under the damp runoff, pebbles fall like rain as you cover your "
        "head to enter..",
        "\nThere is a suspicious hole on the west wall, you fear something may be watching.."
    ]

    return random.choice(descriptions)


def get_generic_actions() -> list:
    """
    Return a list of 97 shuffled action functions.

    :postcondition: returns a list of 97 shuffled action functions
    :return: a list of 97 shuffled action functions
    """
    actions = []

    # 36 battles
    enemy_battles = create_batch_of_enemy_battles(12)
    enemy_battles *= 3
    actions += enemy_battles

    # 36 riddles
    riddles = create_batch_of_riddles(26)
    actions += (riddles + riddles[:11])

    # 13 spider web rooms
    actions += list(itertools.repeat(GenericRooms.spider_web_blockade, 13))

    # 12 empty rooms
    actions += list(itertools.repeat(GenericRooms.empty_room, 12))

    random.shuffle(actions)

    return actions


def main():
    """
    Drive the program.
    """
    print("You are attempting to execute the actions.py module.")
    print("Executing this module does not do anything.")


if __name__ == '__main__':
    main()
