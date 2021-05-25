"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    text = ''
    for i in string:
        if i == '"':
            text += "'"
        elif i == "'":
            text += '"'
        else:
            text += i
    return text
