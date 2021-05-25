"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
#>>> ['donec', 'etiam', 'aliquam']
#> NOTE: Remember about dots, commas, capital letters etc.
"""
from collections import Counter
import re


def most_common_words(text, top_words):
    with open(text, 'r') as file:
        read_file = ''.join(file.readlines())
        text_without_char = re.sub('[!?/()\[\]@#$.,\'\"]', '', read_file.lower())
        arr_for_count = text_without_char.split()

        count_of_word = Counter.most_common(Counter(arr_for_count))

        i = 0
        arr_most_common_words = []
        for word, count in count_of_word:
            while i < top_words:
                arr_most_common_words.append(word)
                i += 1
                break
    return arr_most_common_words

