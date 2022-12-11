"""
The primary game module. Contains the game loop.
"""

from board import Board
from character import Character
from helpers import print_in_color, get_character_name
from actions import cell_description, opening_dialogue, game_completed


def game() -> None:
    """
    Control the flow of the game.

    Create necessary data structures and contain game loop.

    :postcondition: executes the game loop until game is quit or completed
    """
    rows = 10
    columns = 10
    boss_1_coords = (4, 4)
    boss_2_coords = (7, 7)

    board = Board(rows, columns, boss_1_coords, boss_2_coords)

    character_name = get_character_name()
    character = Character(character_name)

    opening_dialogue()
    cell_description()

    achieved_goal = False
    while not achieved_goal:
        board.print_board(character.get_position())
        choice = character.choose_direction(board)

        if choice == "quit":
            break
        elif choice == "show stats":
            character.show_stats()
        elif board.is_valid_move(choice, character):

            character.move(choice, board)

            board.print_board(character.get_position())

            room_solved = board.get_board()[character.get_position()]["solved"]
            if not room_solved:
                board.describe_current_location(character)

                action_function = board.get_board()[character.get_position()]["action"]
                if action_function is not None:
                    board.get_board()[character.get_position()]["solved"] = action_function(character)
            else:
                print_in_color("\nYou have already completed your duties here, please move on.\n", "cyan")

            if character.leveled_up():
                character.level_up_sequence()

            if not character.is_alive():
                character.died()

            achieved_goal = board.boss_defeated()
        else:
            print_in_color("There is no path in that direction, you can't walk through walls!!", "red")

    if achieved_goal:
        game_completed()
        print_in_color("<-------------------------------------Final Stats---------------------------------->", "green")
        character.show_stats()
    else:
        print_in_color("\nThanks for playing, we hope you play again sometime :)", "cyan")


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
