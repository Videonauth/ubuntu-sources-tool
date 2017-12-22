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
__version__ = '0.0.10'

# Program defaults
default_constants = dict(
    DEBUG_MSG=dict(
        NONE=0,
        CRITICAL=1,
        ERROR=2,
        WARN=3,
        ALL=4,
        VAR=5
    ),
)

default_settings = dict(
    DEBUG=False,
    DEBUG_LEVEL=0,
    LOG=False,
    LOG_LEVEL=0
)

if __name__ == '__main__':
    pass
