### A little script to quickly make the 4 files needed
### for each day of AoC with a little boilerplate text
### mostly for a little scripting practice :)
### Pass the day as an argument

import os
import re
import sys

# Check that the argument for the day has been
# provided and is in the expected range, exit if notls
day_to_create = sys.argv[1]

if (
    # make sure it's only digits before typecasting
    not re.match("[0-9]{1,3}", day_to_create)
    # check that the value is a valid AoC day
    or int(day_to_create) > 25
    or int(day_to_create) < 0
):
    print(
        "The argument must be only the digits for the day, for example 5 for December 5th."
    )
    exit()


# Check that we are in the right folder and exit if not
expected_cwd = "C:\\Users\\rache\\Sync\\Formations\\Diginamic\\AoC2023"
if os.getcwd() != expected_cwd:
    print("The script should only be executed in the AoC2023 directory.")
    exit()


data_file_path = f"\\Data\\D{day_to_create}_data.txt"
challenge1_file_path = f"\\Day{day_to_create}_Challenge1.py"
challenge2_file_path = f"\\Day{day_to_create}_Challenge2.py"
readme_file_path = f"\\Day{day_to_create}_Description.md"
files_to_create = [
    data_file_path,
    challenge1_file_path,
    challenge2_file_path,
    readme_file_path,
]

for file_path in files_to_create:
    full_path = f"C:\\Users\\rache\\Sync\\Formations\\Diginamic\\AoC2023{file_path}"
    if os.path.exists(full_path):
        print(f"One or more of the files for day {day_to_create} already exists.")
        exit()

file_open_code = f"""
# Read the input and save it as a list of strings
data: list[str] = []
with open("Data/D{day_to_create}_data.txt") as f:
    data = f.readlines()
"""

readme_header = f"""
# Day {day_to_create}: Advent of Code 2023
"""

for file_path in files_to_create:
    full_path = f"C:\\Users\\rache\\Sync\\Formations\\Diginamic\\AoC2023{file_path}"
    with open(full_path, "w") as f:
        if os.path.exists(full_path):
            print(f"The file {file_path} was successfully created.")
        if file_path in [challenge1_file_path, challenge2_file_path]:
            f.write(file_open_code)
        elif file_path == readme_file_path:
            f.write(readme_header)


print("\n\nHappy coding! Go save Christmas!\n\n")
