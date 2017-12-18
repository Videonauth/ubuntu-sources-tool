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
__version__ = '0.0.5'

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
    DEBUG=True,
    DEBUG_LEVEL=5
)

default_blueprints = dict(
    default_conf=list(f'# config/default.conf file written from default blueprints',
                      f'# version {__version__}',
                      f'DEBUG={eval(default_settings.get("DEBUG"))}',
                      f'DEBUG_LEVEL={eval(default_settings.get("DEBUG_LEVEL"))}'
                      ),
)

if __name__ == '__main__':
    pass
