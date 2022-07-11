import os
from typing import Iterator, List, Iterable, Set, Union
from flask import abort

from constants import COMMANDS, DATA_DIR


def get_args(request_dict):
    """Get arguments from request and check them"""

    file_name = request_dict.get('file_name')
    cmd1 = request_dict.get('cmd1') + '_'
    value1 = request_dict.get('value1')
    cmd2 = request_dict.get('cmd2') + '_'
    value2 = request_dict.get('value2')

    if (
        None in (file_name, cmd1, value1, cmd2, value2)
        or cmd1 not in COMMANDS
        or cmd2 not in COMMANDS
    ):
        return abort(400, 'Wrong params passed')

    file_path = os.path.join(DATA_DIR, file_name)

    if not os.path.exists(file_path):
        return abort(400, 'Wrong filename passed')

    return file_path, cmd1, value1, cmd2, value2


def filter_(iterable: Iterator, string_to_search: str) -> Iterable:
    """Get data which contain specified text"""
    if not isinstance(string_to_search, str):
        raise TypeError("Wrong data passed to the filter function, only strings allowed")
    return filter(lambda line: string_to_search in line, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    """Sort data in ascending or descending order"""
    if order not in ('asc', 'desc'):
        raise ValueError('Wrong argument passed to the sort function, only asc or desc are allowed')
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: Union[str, int]) -> Iterable:
    """Get only column specified"""
    if not str(column).isdigit():
        raise TypeError('Not digit passed as a column number to the map function')
    return map(lambda line: line.split(' ')[int(column)] + '\n', iterable)


def limit_(iterable: Iterator, number: Union[str, int]) -> List:
    """Limit lines returned by the number passed"""
    if not str(number).isdigit():
        raise TypeError('Not digit passed to the limit function, only digits allowed')
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, *args) -> Set:
    """Return only unique lines"""
    return set(iterable)
