"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
#>>> {'o'}
print(chars_in_one(*test_strings))
#>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
#>>> {'h', 'l', 'o'}
print(not_used_chars(*test_strings))
#>>> {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string
from functools import reduce
from itertools import combinations


def chars_in_all(*strings):
    word_sets = [set(word) for word in strings]
    first_word, other_words = word_sets[0], word_sets[1:]
    res = reduce(set.intersection, other_words, first_word)
    return res


def chars_in_one(*strings):
    return set(''.join(strings))


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError('You must have at least two words.')
    word_sets = [set(word) for word in strings]
    comb_two_random_sets = combinations(word_sets, 2)
    new_set = set()
    for i in comb_two_random_sets:
        res = i[0] & i[1]
        new_set.update(res)
    return new_set


def not_used_chars(*strings):
    word_sets = [set(word) for word in strings]
    first_word, other_words = word_sets[0], word_sets[1:]
    res = reduce(set.union, other_words, first_word)

    arr = []
    for letter in string.ascii_lowercase:
        if letter not in res:
            arr.append(letter)
    return set(arr)

