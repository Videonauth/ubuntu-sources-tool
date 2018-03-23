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

from modules.variables import \
    __version__,\
    settings as _settings
from sources_tool import codename

blueprints = dict(
    default_conf=list([
        f'# config/default.conf file written from blueprints',
        f'# version {__version__}',
        f'DEBUG={_settings.get("DEBUG")}',
        f'DEBUG_LEVEL={_settings.get("DEBUG_LEVEL")}',
        f'LOG={_settings.get("LOG")}',
        f'LOG_LEVEL={_settings.get("LOG_LEVEL")}'
    ]),
    sources_list=list([
        f'deb http://archive.ubuntu.com/ubuntu \
        {codename} \
        main restricted universe multiverse',
        f'deb-src http://archive.ubuntu.com/ubuntu \
        {codename} \
        main restricted universe multiverse',
        f'deb http://archive.ubuntu.com/ubuntu \
        {codename}-updates \
        main restricted universe multiverse',
        f'deb-src http://archive.ubuntu.com/ubuntu \
        {codename}-updates \
        main restricted universe multiverse',
        f'deb http://archive.ubuntu.com/ubuntu \
        {codename}-backports \
        main restricted universe multiverse',
        f'deb-src http://archive.ubuntu.com/ubuntu \
        {codename}-backports \
        main restricted universe multiverse',
        f'deb http://archive.ubuntu.com/ubuntu \
        {codename}-security \
        main restricted universe multiverse',
        f'deb-src http://archive.ubuntu.com/ubuntu \
        {codename}-security \
        main restricted universe multiverse',
        f'#deb http://archive.ubuntu.com/ubuntu \
        {codename}-proposed \
        main restricted universe multiverse',
        f'#deb-src http://archive.ubuntu.com/ubuntu \
        {codename}-proposed \
        main restricted universe multiverse',
        f'deb http://archive.canonical.com/ubuntu \
        {codename} \
        partner',
        f'deb-src http://archive.canonical.com/ubuntu \
        {codename} \
        partner'
    ])
)

if __name__ == '__main__':
    pass
