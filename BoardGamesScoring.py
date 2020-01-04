"""A script that enables calculation of points achieved in boardgames by gamers."""

__VERSION__ = '1.0.C'

from my_package.appcli import Cli
from my_package.boardgame import BoardGames


# DEFINED FUNCTIONS

def main():
    """Main function."""
    BG_NAMES = ['Carcassonne',
                'Catan',
                'Power Grid', 'Agricola',
                'Puerto Rico',
                'The Magnates: A Game of Power',
                'Through the Ages: A Story of Civilization',
                'Dominion',
                'Drakon',
                'Fief: France 1429',
                'Scythe',
                'Small World',
                'Splendor',
                'Star Wars: Rebellion',
                'Terraforming Mars',
                'Ticket to Ride: Europe',
                'The Castles of Burgundy']
    cli = Cli()
    cli.clean_console()
    print(f'\nBoardGamesScoring version: {__VERSION__}')
    boardgame = cli.create_choice_menu('Choose a board game:', BG_NAMES, 'Choice:')
    number_of_gamers = input('Enter number of gamers: ')
    names_of_gamers = cli.enter_values('Name of the gamer', number_of_gamers)

    print(boardgame, names_of_gamers)


# MAIN PROGRAM

if __name__ == "__main__":
    main()