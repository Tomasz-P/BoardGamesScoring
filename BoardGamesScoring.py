"""A script that enables calculation of points achieved in boardgames by gamers."""

__VERSION__ = '1.1.C'

from my_package.appcli import Cli
from my_package.boardgame import TerraformingMars


# DEFINED FUNCTIONS

def gameboards_names():
    """Define a list of game boards which can be scored."""
    BG_AVAILABLE_IN_FUTURE = ['Carcassonne',
                              'Catan',
                              'Power Grid',
                              'Agricola',
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
                              'Ticket to Ride: Europe',
                              'The Castles of Burgundy']
    BG_NAMES = ['Terraforming Mars'
                ]
    return BG_NAMES, BG_AVAILABLE_IN_FUTURE

def score_board_game(boardgame, gamers_names):
    """Score points in indicated game board."""
    if boardgame == 'Carcassonne':
        pass
    elif boardgame == 'Catan':
        pass
    elif boardgame == 'Power Grid':
        pass
    elif boardgame == 'Agricola':
        pass
    elif boardgame == 'Puerto Rico':
        pass
    elif boardgame == 'The Magnates: A Game of Power':
        pass
    elif boardgame == 'Through the Ages: A Story of Civilization':
        pass
    elif boardgame == 'Dominion':
        pass
    elif boardgame == 'Drakon':
        pass
    elif boardgame == 'Fief: France 1429':
        pass
    elif boardgame == 'Scythe':
        pass
    elif boardgame == 'Small World':
        pass
    elif boardgame == 'Splendor':
        pass
    elif boardgame == 'Star Wars: Rebellion':
        pass
    elif boardgame == 'Terraforming Mars':
        terraforming_mars = TerraformingMars(gamers_names)
        boardgame_results = terraforming_mars.get_gamers_vps()
        return boardgame_results
    elif boardgame == 'Ticket to Ride: Europe':
        pass
    elif boardgame == 'The Castles of Burgundy':
        pass

def main():
    """Main function."""
    BG_NAMES, BG_AVAILABLE_IN_FUTURE = gameboards_names()
    cli = Cli()
    cli.clean_console()
    print(f'\nBoardGamesScoring version: {__VERSION__}\n---------------------------------')
    boardgame = cli.create_choice_menu('Choose a board game:', BG_NAMES, 'Choice: ')
    number_of_gamers = input('Enter number of gamers: ')
    names_of_gamers = cli.enter_values('Name of the gamer', number_of_gamers)
    boardgame_results = score_board_game(boardgame, names_of_gamers)
    cli.print_game_results(boardgame, boardgame_results)


# MAIN PROGRAM

if __name__ == "__main__":
    main()