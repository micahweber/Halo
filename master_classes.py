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

ranks = [{'int': 1, 'rank': 'Minor', 'color': 'Blue'},
         {'int': 2, 'rank': 'Major', 'color': 'Red'},
         {'int': 3, 'rank': 'Spec Ops', 'color': 'Black'},
         {'int': 4, 'rank': 'Stealth', 'color': 'Camouflage'},
         {'int': 5, 'rank': 'Ultra', 'color': 'Silver'},
         {'int': 6, 'rank': 'General', 'color': 'Gold'},
         {'int': 7, 'rank': 'Honor Guard', 'color': 'Red and Gold'},
         {'int': 8, 'rank': 'Honor Guard Ultra', 'color': 'Silver and Gold'}]


class Rank:
    # Definition for Rank Master Class
    def __init__(self, rank):
        self._rank = rank.title()
        try:
            # get associated integer and aggression level for rank
            self.rank_int = min([rank['int'] for rank in ranks if rank['rank'] == self._rank])
            self.aggression_level = min([rank['int'] for rank in ranks if rank['rank'] == self._rank])
        except (ValueError, KeyError):
            logger.warning(f'Rank {self._rank} not available')
            self.rank_int = 1
            self.aggression_level = 1

        # Determine armor color
        try:
            self.armor_color = min([rank['color'] for rank in ranks if rank['rank'] == self._rank])
        except (ValueError, KeyError):
            logger.warning(f'Rank {self._rank} not available')
            self.armor_color = 'Blue'

    # Define methods for returning Rank attributes
    def get_rank(self):
        return self._rank

    def get_armor_color(self):
        return self.armor_color

    def get_aggression_level(self):
        return self.aggression_level

    # Define other functions for class
    def promote(self):
        self.rank_int += 1

    def demote(self):
        self.rank_int -= 1


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



