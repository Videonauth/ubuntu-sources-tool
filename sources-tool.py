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

# External imports

# Local imports
from modules.core import is_root,\
                         read_file,\
                         write_file

from modules.parser import parser

if __name__ == '__main__':
    commands = parser()
    commands = vars(commands.parse_args())
    print(f'M: {commands}')
    if not commands.get('command') == 'none':
        print(f'M: {commands.get("command")}')
        pass
