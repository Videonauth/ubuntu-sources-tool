#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - parser.py
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 10.12.17 - 15:09
# Purpose: -
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

# External imports
import argparse
import textwrap

# Local imports
from modules.variables import __version__


def parser():
    output = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            Tool for maintaining, creating, repairing and analyzing sources.list files
            """),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    output.add_argument('-b', '--blueprint',
                        type=str,
                        default=None,
                        help='define a blueprint for the command operation.')
    output.add_argument('-c', '--command',
                        type=str,
                        default=None,
                        help='pass command to sources-tool.',
                        nargs='+')
    output.add_argument('-d', '--debug',
                        type=str,
                        default=None,
                        help='define the debug options for sources-tool.')
    output.add_argument('-i', '--in-file',
                        type=str,
                        default=None,
                        help='define the input file for operation.')
    output.add_argument('-l', '--log-file',
                        type=str,
                        default=None,
                        help='define the log file for operation.')
    output.add_argument('-L', '--log-level',
                        type=str,
                        default=None,
                        help='define the log level for operation.')
    output.add_argument('-o', '--out-file',
                        type=str,
                        default=None,
                        help='define the output file for operation.')
    output.add_argument('-r', '--regex-op',
                        type=str,
                        default=None,
                        help='define regex operation.',
                        nargs='+')
    output.add_argument('-V', '--verbose',
                        type=str,
                        default=None,
                        help='define verbosity of sources-tool.')
    output.add_argument("-v", "--version", action="version", version="%(prog)s "+__version__)
    return output


if __name__ == '__main__':
    pass
