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

import os
import datetime


def is_root():
    """Check if the UID of the user running the script is 0 (i.e. root)"""
    if os.getuid() is 0:
        return True
    else:
        return False


def read_file(name):
    """check if the file exists and read it and return a list object"""
    try:
        with open(name) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File Missing: {name}')
        return
    else:
        return list(map(lambda x: x.strip('\n'), lines))


def write_file(name, lines):
    """check if file 'name' not already exists and if not write this file, otherwise make a backup
    of the 'existing' file and then write it """
    lines = list(map(lambda x: f'{x}\n', lines))
    try:
        with open(name, 'x') as file:
            file.writelines(lines)
    except FileExistsError:
        os.rename(name, f'{name}.ust.backup {datetime.datetime.today()}')
        with open(name, 'w') as file:
            file.writelines(lines)


if __name__ == '__main__':
    pass
