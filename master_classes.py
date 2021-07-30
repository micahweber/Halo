""" File for definitions of master classes

@author: Micah Weber <micahe.weber@gmail.com>

@contact: micahe.weber@gmail.com
@github:  https://github.com/micahweber

Revision History
    1.0.0 (2020-11-29, micah.weber) - Initial creation of package

TODO:

Google Python Style Guide: http://google.hithub.io/styleguide/pyguid.html#Python_Style_Rules
Example Google Style Python Docstrings: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""
import argparse
from configparser import ConfigParser
import os
import sys
import time
import logging

logger = logging.getLogger('halo.master_classes')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s'))


class Rank(object):
    ranks = [{'int': 1, 'title': 'Minor', 'color': 'Blue'},
             {'int': 2, 'title': 'Major', 'color': 'Red'},
             {'int': 3, 'title': 'Spec Ops', 'color': 'Black'},
             {'int': 4, 'title': 'Stealth', 'color': 'Camouflage'},
             {'int': 5, 'title': 'Ultra', 'color': 'Silver'},
             {'int': 6, 'title': 'General', 'color': 'Gold'},
             {'int': 7, 'title': 'Honor Guard', 'color': 'Red and Gold'},
             {'int': 8, 'title': 'Honor Guard Ultra', 'color': 'Silver and Gold'}]

    # Definition for Rank Master Class
    def __init__(self, rank='minor'):
        self._rank = rank.title()
        try:
            # get associated integer and aggression level for rank
            self._rank_int = min([rank['int'] for rank in Rank.ranks if rank['title'] == self._rank])
            self._aggression_level = min([rank['int'] for rank in Rank.ranks if rank['title'] == self._rank])
        except (ValueError, KeyError):
            logger.warning(f'Rank {self._rank} not available')
            self._rank_int = 1
            self._aggression_level = 1

        # Determine armor color
        try:
            self._armor_color = min([rank['color'] for rank in Rank.ranks if rank['title'] == self._rank])
        except (ValueError, KeyError):
            logger.warning(f'Rank {self._rank} not available')
            self._armor_color = 'Blue'

    # Define @property and getter for rank
    @property
    def rank(self):
        print('Getting Rank')
        return self._rank

    # Define setter for rank
    @rank.setter
    def rank(self, new_rank):
        print(f'Attempting to set rank to {new_rank}')
        # new_rank must be in Rank.ranks
        is_valid = min([rank['title'] for rank in Rank.ranks if new_rank in rank.values()])
        # if new_rank was in Rank.ranks, it is valid
        if is_valid:
            self._rank = new_rank
            self._rank_int = min(rank['int'] for rank in Rank.ranks if new_rank == rank['title'])
        else:
            self._rank = 'Minor'
            self._rank_int = 1

    # Define @property and getter for rank_int
    @property
    def rank_int(self):
        print('Getting rank as integer')
        return self._rank_int

    # Define setter for rank_int
    @rank_int.setter
    def rank_int(self, new_rank_int):
        print(f'Attempting to set rank_int to {new_rank_int}')
        # new_rank_int must be in ranks
        is_valid = min([rank['int'] for rank in Rank.ranks if new_rank_int in rank.values()])
        # if new_rank_int is in Rank.ranks, it is valid
        if is_valid:
            self._rank_int = new_rank_int
            self._rank = min(rank['title'] for rank in Rank.ranks if new_rank_int == rank['int'])
        else:
            self._rank_int = 1
            self._rank = 'Minor'

    def get_armor_color(self):
        return self.armor_color

    def get_aggression_level(self):
        return self.aggression_level

    # Define other functions for class
    def promote(self):
        if self.rank_int < 8:
            self.rank_int = self._rank_int + 1
        else:
            print('Maximum Rank has been reached')

    def demote(self):
        if self.rank_int > 1:
            self.rank_int = self._rank_int - 1
        else:
            print('Minimum Rank has been reached')


class Enemy:
    # Definition for Enemy Master Class
    def __init__(self, name, rank, faction, health, has_shield, shield_strength, grenade_count=2, *weapons):
        # Unpack arguments into member variables
        self.name = name.title()
        self.rank = rank.rank
        self.armor_color = rank.get_armor_color()
        self.aggression_level = rank.get_aggression_level()
        self.faction = faction
        self.health = health
        self.has_shield = has_shield
        if self.has_shield:
            self.shield_strength = shield_strength
        else:
            self.shield_strength = 0.0
        self.grenade_count = grenade_count
        self.weapons = weapons



