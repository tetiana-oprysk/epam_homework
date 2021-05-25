"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one
at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""
from typing import List


def product_array(num_list: List[int]) -> List[int]:
    new_list = []
    new_list_with_null = num_list.copy()
    multi = 1
    multi_with_null = 1

    for i in num_list:
        multi *= i

    if 0 in new_list_with_null:             # У випадку списку з нулем.
        new_list_with_null.remove(0)
        for i in new_list_with_null:        # Добуток всіх елементів окрім 0.
            multi_with_null *= i

        for i in num_list:
            if i == 0:
                new_list.append(multi_with_null)
            else:
                new_list.append(0)
        return new_list

    for i in range(len(num_list)):
        new_list.append(int(multi / num_list[i]))
    return new_list
