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
from sys import argv

# Local imports
from modules.core import *
from modules.parser import *

# Local variables
MODULE_NAME = 'sources-tool.py'

if __name__ == '__main__':
    # Make protected _parser object and output a dictionary containing
    _parser = parser()
    commands = vars(_parser.parse_args())
    if is_all_none(commands):
        _parser.print_usage()
        exit(0)
    print(os.path.exists(argv[0]))
    print(argv[0])
    # commands.pop('command')
    # commands.update({'command': ['test']})
    # print(commands)
    # if is_all_none(commands):
    #     print(_parser.print_usage())
    #     exit(0)
    # debug(textwrap.dedent(f'\
    #         M: {MODULE_NAME}\n\
    #         V: commands={commands}'
    #                       ),
    #       debugdb.get('DEBUG_ALL')
    #       )
    # if not commands.get('command') == 'none':
    #     debug(textwrap.dedent(f'\
    #             M: {MODULE_NAME}\n\
    #             V: commands.get(\'command\')={commands.get("command")}'
    #             ),
    #           debugdb.get('DEBUG_ALL')
    #           )
    #     is_root()
