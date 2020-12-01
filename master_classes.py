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


class Rank:
    # Definition for Rank Master Class
    def __init__(self, rank):
        self.rank = rank.title()

        # Determine armor color ad aggression level based on rank
        if self.rank == 'Minor':
            self.armor_color = 'Blue'
            self.aggression_level = 1
        elif self.rank == 'Major':
            self.armor_color = 'Red'
            self.aggression_level = 2
        elif self.rank == 'Spec Ops':
            self.armor_color = 'Black'
            self.aggression_level = 3
        elif self.rank == 'Stealth':
            self.armor_color = 'Camouflage'
            self.aggression_level = 4
        elif self.rank == 'Ultra':
            self.armor_color = 'Silver'
            self.aggression_level = 5
        elif self.rank == 'General':
            self.armor_color = 'Gold'
            self.aggression_level = 6
        elif self.rank == 'Honor Guard':
            self.armor_color = 'Red and Gold'
            self.aggression_level = 7
        elif self.rank == 'Honor Guard Ultra':
            self.armor_color = 'Silver and Gold'
            self.aggression_level = 8
        else:
            self.armor_color = 'Blue'
            self.aggression_level = 1

    # Define methods for returning Rank attributes
    def get_rank(self):
        return self.rank

    def get_armor_color(self):
        return self.armor_color

    def get_aggression_level(self):
        return self.aggression_level


class Enemy:
    # Definition for Enemy Master Class
    def __init__(self, name, rank, faction, health, has_shield, shield_strength, grenade_count=2, *weapons):
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


