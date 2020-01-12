"""A module that contains classes, methods, attributes for scoring in board games."""

__VERSION__ = '1.0.0'

from my_package.data_structures_ops import sort_keys_by_value, dict_keys_values_into_two_lists, create_list_matrix

# CLASSES

class TerraformingMars(object):
    """Board games scoring."""

    def __init__(self, gamers_names):
        """Constructor of BoardGames class. Take one argument: 'gamers_names' - a list structure."""
        self.AWARDS = {'Landlord':[5,2],
                       'Banker':[5,2],
                       'Scientist':[5,2],
                       'Thermalist':[5,2],
                       'Miner':[5,2]}
        self.MILESTONES = ['Terraformer',
                           'Mayor',
                           'Gardener',
                           'Builder',
                           'Planner']
        self.MILESTONE_WORTH = 5
        self.gamers_names = gamers_names

    def get_gamers_tr_vps(self):
        """Get Victory Points (VPs) achived by each gamer as Terraforming Rate (TR).
        Return a dictionary.
        """
        gamers_tr_vps = {}
        for gamer_name in self.gamers_names:
            TR_vps = int(input(f'{gamer_name}\'s Terraform Rating (TR): '))
            gamers_tr_vps[gamer_name] = TR_vps
        return gamers_tr_vps

    def get_funded_awards_resources(self):
        """Get resources owned by each gamer corresponding to funded awards during the game."""
        funded_awards_resources = {}
        for award in self.AWARDS.keys():
            answer = ''
            while (answer is not 'y') and (answer is not 'n'):
                answer = input(f'Award "{award}" was funded [y/n]: ')
            if answer == 'y':
                gamers_resources = {}
                for gamer_name in self.gamers_names:
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

    def get_gamers_awards_vps(self):
        """Calculate Victory Points obtained from funded awards resources."""
        funded_awards_resources = self.get_funded_awards_resources()
        gamers_awards_vps = {}
        for funded_award in funded_awards_resources:
            sorted_gamers_by_awards_resources = sort_keys_by_value(funded_awards_resources[funded_award])
            gamers, awards_resources = dict_keys_values_into_two_lists(sorted_gamers_by_awards_resources)
            awards_resources_matrix = create_list_matrix(awards_resources)
            if len(gamers) > 2:
                gamer_award_vps = {}
                for position in range(0, len(awards_resources_matrix)):
                    if awards_resources_matrix[position] == 1:
                        gamer_award_vps[gamers[position]] = self.AWARDS[funded_award][0]
                        gamers_awards_vps[funded_award] = gamer_award_vps
                    elif awards_resources_matrix[position] == 2:
                        gamer_award_vps[gamers[position]] = self.AWARDS[funded_award][1]
                        gamers_awards_vps[funded_award] = gamer_award_vps
                    else:
                        gamer_award_vps[gamers[position]] = 0
                        gamers_awards_vps[funded_award] = gamer_award_vps
            elif len(gamers) == 2:
                gamer_award_vps = {}
                for position in range(0, len(awards_resources_matrix)):
                    if awards_resources_matrix[position] == 1:
                        gamer_award_vps[gamers[position]] = self.AWARDS[funded_award][0]
                        gamers_awards_vps[funded_award] = gamer_award_vps
                    else:
                        gamer_award_vps[gamers[position]] = 0
                        gamers_awards_vps[funded_award] = gamer_award_vps
        return gamers_awards_vps

    def get_gamers_milestones(self):
        """Get milestones claimed during the game by the gamers and return a dictionary
        with gamers' names as keys and lists of claimed milestones by each gamer as
        values.
        """
        milestones_claimed_by_users = {}
        for gamer in self.gamers_names:
            milestones_claimed_by_users.setdefault(gamer, [])
        for milestone in self.MILESTONES:
            for gamer in self.gamers_names:
                answer = ''
                while (answer is not 'y') and (answer is not 'n'):
                    answer = input(f'{gamer} claimed a milestone "{milestone}" [y/n]: ')
                if answer == 'y':
                    milestones_claimed_by_users[gamer].append(milestone)
                    break
        return milestones_claimed_by_users

    def get_gamers_milestones_vps(self):
        """Get milestones Victory Points (VPs) achieved by every gamer."""
        gamers_milestones_vps = {}
        milestones_claimed_by_users = self.get_gamers_milestones()
        for gamer in milestones_claimed_by_users:
            gamers_milestones_vps[gamer] = len(milestones_claimed_by_users[gamer]) * self.MILESTONE_WORTH
        return gamers_milestones_vps

    def get_greenery_tiles(self):
        """Get number of greenery tiles resources on the game board for each gamer."""
        greenery_tiles = {}
        for gamer_name in self.gamers_names:
            greenery_tiles[gamer_name] = int(input(f'Number of {gamer_name}\'s greenery tiles: '))
        return greenery_tiles

    def get_city_tiles(self):
        """Get number of city tiles on the game board for each gamer."""
        city_tiles = {}
        for gamer_name in self.gamers_names:
            city_tiles[gamer_name] = int(input(f'Number of {gamer_name}\'s city tiles: '))
        return city_tiles

    def get_greenery_tiles_adjacent_to_city_tiles(self):
        """Get number of greenery tiles on the game board adjacent to city tiles for each gamer."""
        greenery_tiles_adjacent_to_city_tiles = {}
        city_tiles = self.get_city_tiles()
        for gamer_name in self.gamers_names:
            greenery_tiles_adjacent_to_city_tile = 0
            for city_tile_number in range(1, city_tiles[gamer_name] + 1):
                greenery_tiles_adjacent_to_city_tile += int(input(f'Greenery tiles adjacent to {gamer_name}\'s {city_tile_number}. city tile: '))
            greenery_tiles_adjacent_to_city_tiles[gamer_name] = greenery_tiles_adjacent_to_city_tile
        return greenery_tiles_adjacent_to_city_tiles

    def get_gamers_tiles_vps(self):
        """Get Victory Points (VPs) for tiles resources on the game board for each gamer."""
        tiles_vps = {}
        tiles_vps['greenery_tiles_vps'] = self.get_greenery_tiles()
        tiles_vps['greenery_tiles_adjacent_to_city_tiles_vps'] = self.get_greenery_tiles_adjacent_to_city_tiles()
        return tiles_vps

    def get_gamers_resource_cards_vps(self):
        """Get Victory Points (VPs) claimed from resources cards."""
        gamers_resource_cards_vps = {}
        resource_cards_vps = []
        for gamer_name in self.gamers_names:
            number_of_resource_cards = int(input(f'Number of resource cards claimed by {gamer_name}: '))
            for card_number in range(1, number_of_resource_cards + 1):
                resource_card_vps = int(input(f'Victory Points (VPs) on {gamer_name}\'s {card_number}. resource card: '))
                resource_cards_vps.append(resource_card_vps)
                card_number += 1
            gamers_resource_cards_vps[gamer_name] = resource_cards_vps
            resource_cards_vps = []
        return gamers_resource_cards_vps

    def get_gamers_other_cards_vps(self):
        """Get Victory Points (VPs) claimed from other cards."""
        gamers_other_cards_vps = {}
        other_cards_vps = []
        for gamer_name in self.gamers_names:
            number_of_other_cards = int(input(f'Number of other cards claimed by {gamer_name}: '))
            for card_number in range(1, number_of_other_cards + 1):
                other_card_vps = int(
                    input(f'Victory Points (VPs) on {gamer_name}\'s {card_number}. resource card: '))
                other_cards_vps.append(other_card_vps)
                card_number += 1
            gamers_other_cards_vps[gamer_name] = other_cards_vps
            other_cards_vps = []
        return gamers_other_cards_vps

    def get_gamers_vps(self):
        """Score 'Terraforming Mars' board game for each gamer."""
        print('\nTERRAFORMING RATE\n')
        gamers_tr_vps = self.get_gamers_tr_vps()
        print('\nAWARDS\n')
        gamers_awards_vps = self.get_gamers_awards_vps()
        print('\nMILESTONES\n')
        gamers_milestones_vps = self.get_gamers_milestones_vps()
        print('\nGAME BOARD TILES\n')
        gamers_tiles_vps = self.get_gamers_tiles_vps()
        print('\nRESOURCES CARDS\n')
        gamers_resource_cards_vps = self.get_gamers_resource_cards_vps()
        print('\nOTHER CARDS\n')
        gamers_other_cards_vps = self.get_gamers_other_cards_vps()

        print(gamers_tr_vps)
        print(gamers_awards_vps)
        print(gamers_milestones_vps)
        print(gamers_tiles_vps)
        print(gamers_resource_cards_vps)
        print(gamers_other_cards_vps)