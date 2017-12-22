#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - blueprints.py
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 22.12.17 - 13:48
# Purpose: -
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

from modules.variables import __version__, default_settings

default_blueprints = dict(
    default_conf=list([
        f'# config/default.conf file written from default_blueprints',
        f'# version {__version__}',
        f'DEBUG={default_settings.get("DEBUG")}',
        f'DEBUG_LEVEL={default_settings.get("DEBUG_LEVEL")}'
    ]),
)

if __name__ == '__main__':
    pass
