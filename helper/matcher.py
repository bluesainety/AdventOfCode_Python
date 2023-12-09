import re
from typing import List, Callable, TypeVar

T = TypeVar("T")
O = TypeVar("O")


def find(match: T, coll: List[O], func: Callable[[O], T] = None) -> O:
    return next(f_item for f_item in coll if func(f_item) == match) if func \
        else next(item for item in coll if item == match)


def match_pattern(match_p: re.Pattern, coll: List[O], func: Callable[[O], str] = None) -> O:
    return next(f_item for f_item in coll if re.match(match_p, func(f_item))) if func \
        else next(item for item in coll if re.match(item))


def find_all(match: T, coll: List[O], func: Callable[[O], T] = None) -> [O]:
    return [f_item for f_item in coll if func(f_item) == match] if func \
        else [item for item in coll if item == match]


def match_pattern_all(match_p: re.Pattern, coll: List[O], func: Callable[[O], str] = None) -> [O]:
    return [f_item for f_item in coll if re.match(match_p, func(f_item))] if func \
        else [item for item in coll if re.match(item)]