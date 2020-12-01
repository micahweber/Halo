""" main

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

logger = logging.getLogger('halo.main')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s'))

# Constants
CONNECTION_ERROR_REST_TIME_SECONDS = 15


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/