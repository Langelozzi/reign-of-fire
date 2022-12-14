"""
Module containing the Board class.
"""
import itertools
from helpers import Helpers
from actions import ActionGenerator
from enemies import RoyalMageAngelozzi, LordCommanderYmir, GodKingThompson


class Board:
    """
    A class to represent the game board.
    """

    def __init__(self, rows: int, columns: int, boss_1_coords: tuple, boss_2_coords: tuple) -> None:
        """
        Instantiate a board object of size rows * columns.

        :param rows: a positive integer
        :param columns: a positive integer
        :param boss_1_coords: a tuple of positive non-zero integers both between 1 and rows
        :param boss_2_coords: a tuple of positive non-zero integers both between 1 and rows
        :precondition: rows must be a positive non-zero integer
        :precondition: columns must be a positive non-zero integer
        :precondition: boss_1_coords must be a tuple of positive integers both between 1 and rows
        :precondition: boss_1_coords must be a tuple of positive integers both between 1 and rows
        :postcondition: instantiate a board object of size rows * columns
        """
        if (type(rows) is not int) or (type(columns) is not int):
            raise TypeError("Rows and columns must be integers!")
        if (rows <= 0) or (columns <= 0):
            raise ValueError("Rows and columns must be greater than 0!")

        self.rows = rows
        self.columns = columns
        self.boss_1_coords = boss_1_coords # (4, 4)
        self.boss_2_coords = boss_2_coords # (7, 7)

        self.boss_1 = RoyalMageAngelozzi()
        self.boss_2 = LordCommanderYmir()
        self.final_boss = GodKingThompson()

        self.board = {
            (1, 1): {
                "description": "\nLooks like you have come back to the start, try the opposite direction of the cell",
                "action": None,
                "solved": True,
                "directions": {
                    "north": (1, 2),
                    "east": (2, 1),
                    "south": None,
                    "west": None
                }
            },
            self.boss_1_coords: {
                "description": "\nRoyal Mage Angelozzi, Left Wing of Alyndelle",
                "action": self.boss_1.battle,
                "solved": False,
                "directions": {
                    "north": (4, 5),
                    "east": (5, 4),
                    "south": (4, 3),
                    "west": (3, 4)
                }
            },
            self.boss_2_coords: {
                "description": "\nLord-Commander Ymir, Right Wing of Alyndelle",
                "action": self.boss_2.battle,
                "solved": False,
                "directions": {
                    "north": (7, 8),
                    "east": (8, 7),
                    "south": (7, 6),
                    "west": (6, 7)
                }
            },
            (10, 11): {
                "description": "\nGod-King Thompson, the God Slayer",
                "action": self.final_boss.battle,
                "solved": False,
                "directions": {
                    "north": None,
                    "east": None,
                    "south": (10, 10),
                    "west": None
                }
            }
        }

        actions = itertools.cycle(ActionGenerator.get_generic_actions())

        for x_coord in range(1, self.columns + 1):
            for y_coord in range(1, self.rows + 1):
                if (x_coord == 1 and y_coord == 1) or \
                        (x_coord == 10 and y_coord == 11) or \
                        (x_coord == 4 and y_coord == 4) or \
                        (x_coord == 7 and y_coord == 7):
                    continue

                self.board[(x_coord, y_coord)] = {
                    "description": ActionGenerator.get_generic_room_description(),
                    "action": next(actions),
                    "solved": False,
                    "directions": {
                        "north": (x_coord, y_coord + 1),
                        "east": (x_coord + 1, y_coord),
                        "south": (x_coord, y_coord - 1),
                        "west": (x_coord - 1, y_coord)
                    }
                }

                if x_coord == 1:
                    self.board[(x_coord, y_coord)]["directions"]["west"] = None
                if x_coord == self.rows:
                    self.board[(x_coord, y_coord)]["directions"]["east"] = None
                if y_coord == 1 and x_coord != 1:
                    self.board[(x_coord, y_coord)]["directions"]["south"] = None
                if y_coord == self.columns and x_coord != self.rows:
                    self.board[(x_coord, y_coord)]["directions"]["north"] = None

    def get_board(self):
        """
        Get value of board.

        :postcondition: returns the value of board
        :return: value of board
        """
        return self.board

    def print_board(self, player_coords: tuple):
        """
        Print the board to stdout.

        :param player_coords: a tuple of positive non-zero integers
        :precondition: player_coords must be a tuple of positive non-zero integers
        :postcondition: print a game board indicating the map border, uncleared rooms, sub-bosses and a final boss
        """
        x_pos, y_pos = player_coords
        boss_1_x, boss_1_y = self.boss_1_coords
        boss_2_x, boss_2_y = self.boss_2_coords
        final_boss_x, final_boss_y = (10, 11)

        print()
        for y_coord in range(self.columns + 1, -1, -1):
            for x_coord in range(1, self.rows + 1, 1):
                if y_coord == y_pos and x_coord == x_pos:
                    Helpers.print_in_color('|', "green", end="")
                    Helpers.print_in_color("#", "purple", end="")
                    Helpers.print_in_color('|', "green", end="")

                elif (y_coord == 0 and x_coord == 1) or ((x_coord, y_coord) in self.board.keys()) and \
                        (self.board[(x_coord, y_coord)]["solved"]):
                    Helpers.print_in_color('| |', "green", end="")

                elif (y_coord == boss_1_y and x_coord == boss_1_x) or (y_coord == boss_2_y and x_coord == boss_2_x):
                    Helpers.print_in_color('|', "green", end="")
                    Helpers.print_in_color("X", "red", end="")
                    Helpers.print_in_color('|', "green", end="")

                elif (y_coord == final_boss_y) and (x_coord == final_boss_x):
                    Helpers.print_in_color('|', "green", end="")
                    Helpers.print_in_color("\U0001F451", "red", end="")
                    Helpers.print_in_color('|', "green", end="")

                elif (y_coord == 11 and x_coord != 10) or (y_coord == 0 and x_coord != 1):
                    Helpers.print_in_color('---', "green", end="")

                else:
                    Helpers.print_in_color('|?|', "green", end="")

            print()

    def describe_current_location(self, character) -> None:
        """
        Print the description of the room that the player is currently in.

        :param character: a character object
        :precondition: character must be a character object
        :postcondition: prints the content of the key "description" from self.board dictionary
        :postcondition: character object passed through this function will remain unchanged
        """
        current_position = character.get_position()
        Helpers.print_in_color(self.board[current_position]["description"], "cyan")

    def is_valid_move(self, direction: str, character) -> bool:
        """
        Determine if the user input for player movement is valid.

        :param direction: one of the following strings in lowercase: "north", "east", "south", "west"
        :param character: a Character object
        :precondition: direction must be the following strings in lowercase: "north", "east", "south", "west"
        :precondition: character must be a Character object
        :postcondition: return True if an x or y coordinates of a next move exists; else False
        :postcondition: parameters passed through this function will remain unchanged
        :return: True if an x or y coordinates of a next move exists; else False if the next coordinate has
                 None value
        """
        current_position = character.get_position()
        try:
            if self.board[current_position]["directions"][direction] is not None:
                return True
        except KeyError:
            return False
        else:
            return False

    def boss_defeated(self) -> bool:
        """
        Determine if the final boss is defeated.

        :postcondition: return True if a value tied to the 'solved' key in board is
                        True; else False
        :return: True if a value tied to the 'solved' key in board[(10,11)] is True; else False

        >>> test_board = { (10, 11): {"description": "God-King Thompson, the God Slayer", "action": self.final_boss.battle(), "solved": False, "directions": {"north": None, "east": None, "south": (10, 10), "west": None} } }
        >>> self.boss_defeated(test_board)
        False
        """
        return True if self.board[(10, 11)]['solved'] else False


def main():
    """
    Drive the Program.
    """
    print("You are attempting to execute the board.py module.")
    print("Executing this module does not do anything.")


if __name__ == '__main__':
    main()
