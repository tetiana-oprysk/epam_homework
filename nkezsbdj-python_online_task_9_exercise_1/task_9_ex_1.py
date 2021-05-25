"""
Task_9_1
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


def swap_quotes(some_string: str) -> str:
    old_quotes = "\'\""
    new_quotes = "\"\'"
    tr_tab = some_string.maketrans(old_quotes, new_quotes)
    return some_string.translate(tr_tab)
