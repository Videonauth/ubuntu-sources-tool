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
import sys

# Local imports
from modules.core import *
from modules.parser import *

if __name__ == '__main__':
    commands = parser()
    commands = vars(commands.parse_args())
    debug(textwrap.dedent(f'\
            M: {sys.argv[0]}\n\
            V: commands={commands}'
            ),
          DEBUG_ALL
          )
    if not commands.get('command') == 'none':
        debug(textwrap.dedent(f'\
                M: {sys.argv[0]}\n\
                V: commands.get(\'command\')={commands.get("command")}'
                ),
              DEBUG_ALL
              )
