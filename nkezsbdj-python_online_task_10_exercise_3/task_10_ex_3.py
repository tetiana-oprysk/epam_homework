"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)

        arr = []
        for line in csv_reader:
            arr.append(line)

        arr.remove(['student name', 'age', 'average mark'])
        csv_reader_sort = sorted(arr, key=lambda s: float(s[2]), reverse=True)

        top_students = []
        i = 0
        for name, age, points in csv_reader_sort:
            while i < number_of_top_students:
                top_students.append(name)
                i += 1
                break
        return top_students


def write_students_age_desc(file_path, output_file):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        csv_reader_sort = sorted(csv_reader, key=lambda s: s['age'], reverse=True)

        with open(output_file, 'w') as new_csv_file:
            desc_of_columns = ['student name', 'age', 'average mark']
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=desc_of_columns)

            csv_writer.writeheader()

            for row in csv_reader_sort:
                csv_writer.writerow(row)
