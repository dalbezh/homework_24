import re
from typing import Iterable, List, Any, Set, Dict, Callable, Optional


def filter_query(value: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    if value == 'desk':
        return sorted(data, reverse=True)
    else:
        return sorted(data)


def regex_query(value: str, data: Iterable[str]) -> Iterable[str]:
    pattern = re.compile(value)
    print(pattern)
    return filter(lambda x: re.search(pattern, x), data)


command: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query
}


def read_file(file: str) -> Iterable[str]:
    with open(file, "r", encoding='utf-8') as f:
        for line in f:
            yield line


def build_query(cmd: str, value: str, file: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        preparing_data = read_file(file)
    else:
        preparing_data = data
    return list(command[cmd](value=value, data=preparing_data))
