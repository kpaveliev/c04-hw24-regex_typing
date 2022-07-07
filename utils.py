from typing import Iterator, List, Iterable, Set


def filter_(iterable: Iterator, string_to_search: str) -> Iterable:
    """Get data which contain specified text"""
    return filter(lambda line: string_to_search in line, iterable)


def sort_(iterable: Iterator, order: str = 'asc') -> List:
    """Sort data in ascending or descending order"""
    if order == 'desc':
        return sorted(iterable, reverse=True)
    return sorted(iterable, reverse=False)


def map_(iterable: Iterator, column: str) -> Iterable:
    """Get only column specified"""
    return map(lambda line: line.split(' ')[int(column)] + '\n', iterable)


def limit_(iterable: Iterator, number: str) -> List:
    """Limit lines returned by the number passed"""
    return list(iterable)[:int(number)]


def unique_(iterable: Iterator, value=None) -> Set:
    """Return only unique lines"""
    return set(iterable)
