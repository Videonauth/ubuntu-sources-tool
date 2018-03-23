#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - sources-tool
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 10.12.17 - 11:08
# Purpose: maintaining sources.list files (analyzing, repairing, changing)
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

"""Tool for maintaining sources.list files (analyzing, repairing, changing)"""

# External imports
import time
import os

# Local imports
from modules.variables import \
    settings as _settings, \
    distributions_names as _distribution_names
from modules.blueprints import \
    blueprints as _blueprints
from modules.core import \
    dict_is_all_none, \
    file_to_dict, \
    list_to_file, \
    file_exists, \
    strip_quotes_from_dict, \
    list_to_stdout, \
    end_program
from modules.parser import \
    parser

# Local variables
_time = time.time()
_path = os.path.dirname(os.path.realpath(__file__))
_file = 'sources_tool.py'


# global class Parameter is a data container
class Parameter:
    def __init__(self):
        # Getting and parsing system information in to a dictionary called i_lsb_release which is meant to be private.
        # We only 'read' here, since we clean the input, writing it back could be fatal! If the file not exists,
        # we have a very dire dependency fail and exit out with error.
        i_lsb_release = dict()
        if file_exists(f'/etc/lsb-release'):
            i_lsb_release.update(strip_quotes_from_dict(file_to_dict(f'/etc/lsb-release')))
        else:
            print(f'File \"/etc/lsb-release\" missing, aborting action.')
            end_program(_time, 2, time.time())

        # transferring the read in data from i_lsb_release into class variables
        self.DISTRIB_ID = i_lsb_release.get('DISTRIB_ID')
        self.DISTRIB_RELEASE = i_lsb_release.get('DISTRIB_RELEASE')
        self.DISTRIB_CODENAME = i_lsb_release.get('DISTRIB_CODENAME')
        self.DISTRIB_DESCRIPTION = i_lsb_release.get('DISTRIB_DESCRIPTION')

        # checking if the read in distribution codename is in the list of supported releases.
        if self.DISTRIB_CODENAME not in _distribution_names:
            print(f'Unknown distribution, aborting action.')
            end_program(_time, 3, time.time())

    def set_id(self, distribution_id):
        self.DISTRIB_ID = distribution_id

    def set_release(self, release):
        self.DISTRIB_RELEASE = release

    def set_codename(self, codename):
        self.DISTRIB_CODENAME = codename

    def set_description(self, description):
        self.DISTRIB_DESCRIPTION = description

    def get_id(self):
        return self.DISTRIB_ID

    def get_release(self):
        return self.DISTRIB_RELEASE

    def get_codename(self):
        return self.DISTRIB_CODENAME

    def get_description(self):
        return self.DISTRIB_DESCRIPTION


_parameter = Parameter()

if __name__ == '__main__':
    # Create an argparse parser object and uses it to fetch command-line options in a directory.
    _parser = parser()
    _commands = vars(_parser.parse_args())

    # Check command-line options if any are given, if not print usage and exit out.
    if dict_is_all_none(_commands):
        _parser.print_usage()
        print(f'No commands given.')
        end_program(_time, 0, time.time())

    # Check if 'default.conf' exists and if yes read it, if not use default rom variables and write file.
    # The situation of a missing default.conf file should not happen leaving the function in for the rare
    # occurrence of the user deleting the file, then writing a new one from _blueprints.get('default_conf')
    if file_exists(f'{_path}/config/default.conf'):
        _settings.update(file_to_dict(f'{_path}/config/default.conf'))
    else:
        list_to_file(_blueprints.get('default_conf'), f'{_path}/config/default.conf')

    list_to_stdout(_blueprints.get('sources_list'))
    print(_parameter.DISTRIB_ID)
    print(_parameter.DISTRIB_RELEASE)
    print(_parameter.DISTRIB_CODENAME)
    print(_parameter.DISTRIB_DESCRIPTION)
    
    # Reached the end of the file exiting.
    print(f'Natural program end reached.')
    end_program(_time, 0, time.time())
