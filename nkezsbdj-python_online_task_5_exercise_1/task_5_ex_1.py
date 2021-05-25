"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum


class SortOrder(Enum):
    ascending = 'ascending'
    descending = 'descending'


def is_sorted(num_list: list[int], sort_order: SortOrder) -> bool:
    if not all((isinstance(num, int) for num in num_list)) or \
         not isinstance(sort_order, SortOrder):
        raise TypeError
    if sort_order.value == 'ascending':
        return True if num_list == sorted(num_list) else False

    elif sort_order.value == 'descending':
        return True if num_list == sorted(num_list, reverse=True) else False

    else:
        raise TypeError


def transform(num_list: list[int], sort_order: SortOrder) -> list[int]:
    new_num_list = []
    if not all((isinstance(num, int) for num in num_list)) or \
         not isinstance(sort_order, SortOrder):
        raise TypeError
    if is_sorted(num_list, sort_order):
        for i in num_list:
            new_num_list.append((i+num_list.index(i)))
        return new_num_list
    else:
        return num_list
