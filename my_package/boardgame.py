"""A module that contains classes, methods, attributes for scoring in board games."""

__VERSION__ = '1.0.0'

from my_package.dir_operations import inner_to_outer_dir

# CLASSES

class TerraformingMars(object):
    """Board games scoring."""

    def __init__(self):
        """Constructor of BoardGames class."""
        self.AWARDS = {'Landlord':[5,2],
                       'Banker':[5,2],
                       'Scientist':[5,2],
                       'Thermalist':[5,2],
                       'Miner':[5,2]}
        self.MILESTONES = {'Terraformer':5,
                           'Mayor':5,
                           'Gardener':5,
                           'Builder':5,
                           'Planner':5}

    def get_gamers_tr_vps(self, gamers_names_list):
        """Get Victory Points (VPs) for each gamer. Return a directory."""
        gamers_tr_vps = {}
        for gamer_name in gamers_names_list:
            TR_vps = int(input(f'{gamer_name}\'s Terraform Rating (TR): '))
            gamers_tr_vps[gamer_name] = TR_vps
        return gamers_tr_vps

    def get_funded_awards_resources(self, gamers_names_list):
        """Get three funded awards during the game."""
        funded_awards_resources = {}
        for award in self.AWARDS.keys():
            answer = ''
            while (answer is not 'y') and (answer is not 'n'):
                answer = input(f'Award "{award}" was funded [y/n]: ')
            if answer == 'y':
                gamers_resources = {}
                for gamer_name in gamers_names_list:
                    if award == 'Landlord':
                        tiles_in_play = int(input(f'Enter {gamer_name}\'s total number of tiles in play: '))
                        gamers_resources[gamer_name] = tiles_in_play
                    elif award == 'Banker':
                        megacredits_production = int(input(f'Enter {gamer_name}\'s megacredists production: '))
                        gamers_resources[gamer_name] = megacredits_production
                    elif award == 'Scientist':
                        science_tags_in_play = int(input(f'Enter {gamer_name}\'s science tag in play: '))
                        gamers_resources[gamer_name] = science_tags_in_play
                    elif award == 'Thermalist':
                        heat_resource_cubes = int(input(f'Enter {gamer_name}\'s heat resource cubes: '))
                        gamers_resources[gamer_name] = heat_resource_cubes
                    elif award == 'Miner':
                        steel_and_titanium_resource_cubes = int(input(f'Enter {gamer_name}\'s steel and titanium resource cubes: '))
                        gamers_resources[gamer_name] = steel_and_titanium_resource_cubes
                funded_awards_resources[award] = gamers_resources
        return funded_awards_resources

    def get_gamers_awards_vps(self, gamers_awards_resources):
        """Calculate Victory Points obtained from funded awards resources."""
        pass

    def get_claimed_milestones(self, gamer_name):
        """Get milestones claimed during the game."""
        milestones_claimed = []
        for milestone in self.MILESTONES.keys():
            answer = ''
            while (answer is not 'y') and (answer is not 'n'):
                answer = input(f'Milestone "{milestone}" claimed [y/n]: ')
            if answer == 'y':
                milestones_claimed.append(milestone)
        return milestones_claimed

    def get_milestones_vps(self, claimed_milestones):
        """Get milestones Victory Points (VPs)."""
        milestones_vps = 0
        for milestone in claimed_milestones:
            milestones_vps += self.MILESTONES[milestone]
        return milestones_vps

    def get_gameboard_vps(self, game_namer):
        """Get victory points (VPs) claimed from the map on the game board."""
        greenery_tiles_vps = int(input(f'\nNumber of {game_namer}\'s greenery tiles: '))
        city_tiles = int(input(f'Number of {game_namer}\'s city tiles: '))
        greenery_tiles_adjacent_to_city_tile_vps = 0
        for city_tile_number in range(1, city_tiles + 1):
            greenery_tiles_adjacent_to_city_tile_vps += int(input(f'Greenery tiles adjacent to {city_tile_number}. city tile: '))
        return greenery_tiles_vps, greenery_tiles_adjacent_to_city_tile_vps

    def get_gamer_achievements(self, gamers_names):
        """Score 'Terraforming Mars' board game."""
        print('\nTERRAFORMING RATE\n')
        gamers_tr_vps = self.get_gamers_tr_vps(gamers_names)
        print(gamers_tr_vps)
        print('\nAWARDS\n')
        gamers_awards_resources = self.get_funded_awards_resources(gamers_names)
        print(gamers_awards_resources)
        print('\nMILESTONES\n')
        milestones_vps = self.get_milestones_vps(self.get_claimed_milestones(gamer_name))
        print('\nGAME BOARD TILES')
        greenery_tiles_vps, greenery_tiles_adjacent_to_city_tile_vps = self.get_gameboard_vps(gamer_name)
        print('\nRESOURCES CARDS\n')
        resources_cards_vps = int(input(f'Resources cards Victory Points (VPs): '))
        print('\nCARDS\n')
        cards_vps = int(input(f'Cards Victory Points (VPs): '))
        return TR_vps, gamers_awards_resources, milestones_vps, greenery_tiles_vps, greenery_tiles_adjacent_to_city_tile_vps,\
               resources_cards_vps, cards_vps