#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - core.py
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 10.12.17 - 11:20
# Purpose: -
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

# External imports
import os
import datetime
# import textwrap

# Local imports
from modules.variables import debugdb

# Local variables
MODULE_NAME = 'modules/core.py'


def debug(message, level):
    """Provides debugging output if DEBUG is True and level is smaller or equal to DEBUG_LEVEL

    :param message: formatted string variable
    :param level: integer value to be challenged by DEBUG_LEVEL
    :returns None:
    """
    if debugdb.get('DEBUG'):
        if level <= debugdb.get('DEBUG_LEVEL'):
            _date = datetime.datetime.today()
            if level == debugdb.get('DEBUG_ALL'):
                _level = 'DEBUG_ALL'
            if level == debugdb.get('DEBUG_WARN'):
                _level = 'DEBUG_WARN'
            if level == debugdb.get('DEBUG_ERROR'):
                _level = 'DEBUG_ERROR'
            if level == debugdb.get('DEBUG_CRITICAL'):
                _level = 'DEBUG_CRITICAL'
            if level == debugdb.get('DEBUG_NONE'):
                _level = 'DEBUG_NONE'
            if debugdb.get('DEBUG_LEVEL') == debugdb.get('DEBUG_ALL'):
                _Level = 'DEBUG_ALL'
            if debugdb.get('DEBUG_LEVEL') == debugdb.get('DEBUG_WARN'):
                _Level = 'DEBUG_WARN'
            if debugdb.get('DEBUG_LEVEL') == debugdb.get('DEBUG_ERROR'):
                _Level = 'DEBUG_ERROR'
            if debugdb.get('DEBUG_LEVEL') == debugdb.get('DEBUG_CRITICAL'):
                _Level = 'DEBUG_CRITICAL'
            if debugdb.get('DEBUG_LEVEL') == debugdb.get('DEBUG_NONE'):
                _Level = 'DEBUG_NONE'
            output = f'{_date}\nD: [{level}]: {_level} [{debugdb.get("DEBUG_LEVEL")}]: {_Level}\n{message}'
            print(output)
            return
        else:
            return
    else:
        return


def is_all_none(dictionary):
    """Test if all entries in dictionary have the value 'none'

    :param dictionary: command line parameters as a dictionary
    :returns boolean: True if all entries in dictionary are 'none'

    :debug DISABLED
    """
    for x, y in dictionary.items():
        # debug(textwrap.dedent(f'\
        #         M: {MODULE_NAME}\n\
        #         F: is_all_none()\n\
        #         V: x={x}\n\
        #         V: y={y}'
        #                       ),
        #       debugdb.get('DEBUG_ALL')
        #       )
        if not y == 'none':
            # debug(textwrap.dedent(f'\
            #         M: {MODULE_NAME}\n\
            #         F: is_all_none()\n\
            #         O: in KEY x={x}, VALUE for y={y} is not "none". Returning False'
            #                       ),
            #       debugdb.get('DEBUG_ALL')
            #       )
            return False
    # debug(textwrap.dedent(f'\
    #         M: {MODULE_NAME}\n\
    #         F: is_all_none()\n\
    #         O: all VALUE are "none". Returning True'
    #                       ),
    #       debugdb.get('DEBUG_ALL')
    #       )
    return True


def is_root():
    """Check if the UID of the user running the script is 0 (i.e. root)

    :param None:
    :returns boolean: True or False depending if the UID using the script is 0:root

    :debug DISABLED
    """
    if os.getuid() is 0:
        # debug(textwrap.dedent(f'\
        #         M: {MODULE_NAME}\n\
        #         F: is_root()\n\
        #         V: os.getuid()={os.getuid()}\n\
        #         O: UID == 0 returning True'
        #                       ),
        #       debugdb.get('DEBUG_ALL')
        #       )
        return True
    else:
        # debug(textwrap.dedent(f'\
        #         M: {MODULE_NAME}\n\
        #         F: is_root()\n\
        #         V: os.getuid()={os.getuid()}\n\
        #         O: UID != 0 returning False'
        #                       ),
        #       debugdb.get('DEBUG_ALL')
        #       )
        return False


def strip_newline(lines):
    return list(map(lambda x: x.strip('\n'), lines))


def append_newline(lines):
    return list(map(lambda x: f'{x}\n', lines))


def read_file(name):
    """check if the file exists and read it and return a list object"""
    try:
        with open(name) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'File missing: {name}')
        exit(1)
    except PermissionError:
        print(f'Permissions missing for file: {name}')
        exit(1)
    else:
        return strip_newline(lines)


def write_file(name, lines):
    """check if file 'name' not already exists and if not write this file, otherwise make a backup
    of the 'existing' file and then write it """
    lines = append_newline(lines)
    try:
        with open(name, 'x') as file:
            file.writelines(lines)
    except FileExistsError:
        try:
            os.rename(name, f'{name}.ust.backup {datetime.datetime.today()}')
            with open(name, 'w') as file:
                file.writelines(lines)
        except PermissionError:
            print(f'Permissions missing for file: {name}')
            exit(1)
        else:
            return True
    except PermissionError:
        print(f'Permissions missing for file: {name}')
        exit(1)
    else:
        return True


if __name__ == '__main__':
    pass
