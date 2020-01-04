"""A module that contains methods, attributes for creating and managing command line interface."""

__VERSION__ = '1.0.0'

from platform import system
from subprocess import run


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

    def create_choice_menu(self, entry_text, positions):
        """Create a menu consisting of an entry text and a number of positions given by
         a python list.
         """
        menu_string = '\n' + entry_text + '\n\n'
        number = 1
        for position in sorted(positions):
            number_of_spaces = len(str(len(positions))) + 1 - len(str(number))
            menu_string += f'{number})' + number_of_spaces * ' ' + f'{position}\n'
            number += 1
        return menu_string

    def enter_values(self, text, number_of_texts):
        """Enter one value and return the value."""
        for number in range(1, int(number_of_texts) + 1):
            value = input(text + ' ' + str(number) + ': ')
        return value