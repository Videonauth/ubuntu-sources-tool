#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ---------------------------------------------------------------------------
# ubuntu-sources-tool - core.py
# ---------------------------------------------------------------------------
# Author: Videonauth <videonauth@googlemail.com>
# License: MIT (see LICENSE file)
# Date: 10.12.17 - 11:20
# Purpose: -
# Written for: Python 3.6.3
# ---------------------------------------------------------------------------

# External imports
import os
import datetime
# import textwrap

# Local imports
# from modules.variables import debug_settings

# Local variables
MODULE_NAME = 'modules/core.py'


def strip_newline(lines):
    return list(map(lambda x: x.strip('\n'), lines))


def append_newline(lines):
    return list(map(lambda x: f'{x}\n', lines))


def dict_to_list(dictionary_item, delimiter='='):
    _output = []
    for _key, _value in dictionary_item.items():
        _output.append(f'{_key}{delimiter}{_value}')
    return _output


def dict_get_key_for_value(dictionary_item, value):
    for _key, _value in dictionary_item.items():
        if _value == value:
            return _key
    return None


def dict_get_value_for_key(dictionary_item, key):
    for _key, _value in dictionary_item.items():
        if _key == key:
            return _value
    return None


def dict_is_all_none(dictionary_item):
    for _key, _value in dictionary_item.items():
        if _value is not None:
            return False
    return True


def file_to_list(name):
    try:
        with open(name) as _file:
            _lines = _file.readlines()
    except PermissionError as error:
        print(f'{datetime.datetime.today()} {error}')
        exit(1)
    except FileNotFoundError as error:
        print(f'{datetime.datetime.today()} {error}')
        exit(1)
    else:
        return strip_newline(_lines)


def list_to_dict(list_item, delimiter='='):
    _output = dict()
    for _line in list_item:
        if not _line[0] == '#':
            _output.update(
                {_line.split(delimiter)[0]: eval(_line.split(delimiter)[1])}
            )
    return _output


def file_exists(name):
    return os.path.exists(name)


def file_to_dict(name):
    return list_to_dict(file_to_list(name))


def list_to_file(list_item, name):
    list_item = append_newline(list_item)
    try:
        with open(name, 'x') as file:
            file.writelines(list_item)
    except FileExistsError:
        try:
            os.rename(name, f'{name}.backup {datetime.datetime.today()}')
            with open(name, 'w') as file:
                file.writelines(list_item)
        except PermissionError:
            print(f'Permissions missing for file: {name}')
            exit(1)
        else:
            return True
    except PermissionError:
        print(f'Permissions missing for file: {name}')
        exit(1)
    else:
        return True


def dict_to_file(dictionary_item, name):
    list_to_file(dict_to_list(dictionary_item), name)


def is_root():
    if os.getuid() is 0:
        return True
    else:
        return False


if __name__ == '__main__':
    pass
