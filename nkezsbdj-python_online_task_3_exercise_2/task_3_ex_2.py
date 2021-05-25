"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('roman_number', type=str)


def from_roman_numerals(args):
    roman_numeral = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     }

    number = []
    for i in args:
        if i in roman_numeral.keys():
            number.append(roman_numeral[i])
        else:
            raise ValueError('Incorrect data entry.')

    none_numbers = []
    for n in range(len(number)-1):
        if number[n] < number[(n+1)]:
            number.append(number[n + 1] - number[n])
            none_numbers.append(number[n+1])
            none_numbers.append(number[n])
    # print(number)
    # print(none_numbers)
    # print(sum([x for x in number if x not in none_numbers]))
    return sum([x for x in number if x not in none_numbers])


def main():
    args = parser.parse_args()
    print(from_roman_numerals(args.roman_number))


if __name__ == "__main__":
    main()
