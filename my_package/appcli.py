"""A module that contains methods, attributes for creating and managing command line interface."""

__VERSION__ = '1.1.0'

from platform import system
from subprocess import run
from my_package.data_structures_ops import sort_keys_by_value, dict_keys_values_into_two_lists


# CLASSES

class Cli(object):
    """Management of command line interface."""

    def __init__(self):
        """A Cli() class constructor."""

    def clean_console(self):
        """Clean console in Windows, Linux, MacOS."""
        if system() == 'Windows':
            run(['cls'], shell=True)
            return 0
        elif system() == 'Linux' or system() == 'Darwin':
            run(['clear'], shell=True)
            return 0
        else:
            print('Sorry, console cannot be cleared. System platform not recognized.')
            return 1

    def create_choice_menu(self, entry_text, positions, choice_text):
        """Create a menu consisting of an entry text, a number of positions given by
         a python list and a choice text. Return the text of chosen position.
         """
        positions_dict = {}
        menu_string = '\n' + entry_text + '\n\n'
        number = 1
        for position in sorted(positions):
            number_of_spaces = len(str(len(positions))) + 1 - len(str(number))
            menu_string += f'{number})' + number_of_spaces * ' ' + f'{position}\n'
            positions_dict[number] = position
            number += 1
        print(menu_string)
        choice = int(input(choice_text))
        return positions_dict[choice]

    def enter_values(self, text, number_of_texts):
        """Enter next values and return the list of enterred values."""
        values = []
        for number in range(1, int(number_of_texts) + 1):
            value = input(text + ' ' + str(number) + ': ')
            values.append(value)
        return values

    def print_game_results(self, boardgame, gamers_vps):
        """Print names of gamers and victory points (VPs) obtained by them."""
        gamers, vps = dict_keys_values_into_two_lists(sort_keys_by_value(gamers_vps))
        print(f'\n\n{boardgame.upper()} - Victory Points\n')
        for gamers_name in gamers_vps.keys():
            print(f'{gamers_name}  -  {gamers_vps[gamers_name]}')
        if len(gamers) > 1:
            print(f'\nThe winner is {gamers[0]} with {vps[0]} VPs.')
        return 0