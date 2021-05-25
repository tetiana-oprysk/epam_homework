"""
Implement a function `split_by_index(string: str, indexes: List[int]) -> List[str]`
which splits the `string` by indexes specified in `indexes`. 
Only positive index, larger than previous in list is considered valid.
Invalid indexes must be ignored.

Examples:
```python
#>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("no luck", [42])
["no luck"]
```
"""


def split_by_index(string, indexes):
    unique = []

    for number in indexes:
        if number in unique:
            continue
        elif isinstance(number, int):
            unique.append(number)

    valid_indexes = []
    current_index = 0

    for index in range(len(unique)):
        valid_indexes.append(unique[current_index])

        if unique[index] == 0:
            unique.remove(unique[index])

        if unique[index] > unique[current_index]:
            current_index = unique.index(unique[index])

    if unique[-1] > valid_indexes[-1]:
        valid_indexes.append(unique[-1])

    new_indexes = sorted(list(set(valid_indexes)))

    st = [string[0:new_indexes[0]]]
    parts = [string[i:j] for i, j in zip(new_indexes, new_indexes[1:] + [None])]
    return st+parts
