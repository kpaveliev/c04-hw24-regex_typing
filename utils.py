from typing import Iterator, List, Iterable, Set, Union


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
