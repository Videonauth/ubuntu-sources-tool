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

from modules.parser import make_parser,\
                           sanitize_input

if __name__ == '__main__':
    # if not is_root():
    #     print('E: Missing privileges! Are you root?')
    # else:
    #     commands = make_parser()
    #     print(commands.parse_args())
    src_lst = read_file('/etc/apt/sources.list')
    # print(src_lst)
    write_file('./sources.list', src_lst)
    # write_file('/etc/apt/sources.list', src_lst)
