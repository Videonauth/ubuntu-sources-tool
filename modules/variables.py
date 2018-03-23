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
constants = dict(
    DEBUG_MSG=dict(
        NONE=0,
        CRITICAL=1,
        ERROR=2,
        WARN=3,
        ALL=4,
        VAR=5
    ),
)

settings = dict(
    DEBUG=False,
    DEBUG_LEVEL=0,
    LOG=False,
    LOG_LEVEL=0,
)

distributions_names = list([
    'artful',
    'bionic',
    'zesty',
    'trusty',
])

# $ cat /etc/apt/sources.list
# deb http://archive.ubuntu.com/ubuntu artful main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu artful main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu artful-updates main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu artful-updates main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu artful-backports main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu artful-backports main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu artful-security main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu artful-security main restricted universe multiverse
# deb http://archive.ubuntu.com/ubuntu artful-proposed restricted main universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu artful-proposed restricted main universe multiverse
# deb http://archive.canonical.com/ubuntu artful partner
# deb-src http://archive.canonical.com/ubuntu artful partner

# link_settings = dict(
#     main_link="http://archive.ubuntu.com",
#
# )

if __name__ == '__main__':
    pass
