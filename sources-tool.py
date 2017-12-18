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

# Local imports
from modules.variables import *
from modules.core import *
from modules.parser import *

# Local variables
_time = time.time()
_path = os.path.dirname(os.path.realpath(__file__))
_file = 'sources-tool.py'

if __name__ == '__main__':
    # Create an argparse parser object and uses it to fetch command-line options in a directory.
    _parser = parser()
    _commands = vars(_parser.parse_args())

    # Check command-line options if any are given, if not print usage and exit out.
    if dict_is_all_none(_commands):
        _parser.print_usage()
        print(f'Process finished after {time.time() - _time} seconds.')
        print(f'Process finished with exit code 0.')
        exit(0)

    # Check if 'default.conf' exists and if yes read it, if not use default from variables and write file.
    _settings = default_settings
    if file_exists(f'{_path}/config/default.conf'):
        _settings.update(file_to_dict(f'{_path}/config/default.conf'))
    # else:
    #     dict_to_file(_settings, f'{_path}/config/default.conf')

    # Reached the end of the file exiting.
    print(f'Process finished after {time.time() - _time} seconds.')
    print(f'Process finished with exit code 0.')
    exit(0)
