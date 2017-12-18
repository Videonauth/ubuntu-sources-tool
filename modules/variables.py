#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - variables.py
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 10.12.17 - 15:33
# Purpose: -
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

# Version string
__version__ = '0.0.3'

# DEBUG-OPTIONS
default_settings = dict(
    DEBUG=True,
    DEBUG_MSG=dict(
                   NONE=0,
                   CRITICAL=1,
                   ERROR=2,
                   WARN=3,
                   ALL=4,
                   VAR=5
                   ),
    DEBUG_LEVEL=5
)
settings = {'log_file': 'none',
            'log_level': 'none'
            }

if __name__ == '__main__':
    pass
