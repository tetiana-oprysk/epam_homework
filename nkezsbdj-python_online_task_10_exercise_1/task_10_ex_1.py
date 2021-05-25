"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, 'r') as input_file:
        names = input_file.readlines()
        s_names = sorted(names)
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(s_names)
