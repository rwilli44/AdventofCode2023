import re
from typing import Iterator, Match

# Read the input and save it as a list of strings
data: list[str] = []

with open("Data/D11_data.txt") as f:
    data = f.readlines()
    for i, row in enumerate(data):
        data[i] = row.strip()


def check_no_galaxies(column_index: int, star_map: list[str]) -> bool:
    """This function checks the given column index in each row. If any galaxies
    identified by '#' are found in the column, return False. Otherwise return
    true.

    Args:
        column_index (int): a digit representing the column in a map
        star_map (list[str]): a list of strings which make up the "star chart"

    Returns:
        bool: True if no galaxies are found, false otherwise.
    """
    for row in star_map:
        if row[column_index] == "#":
            return False
    return True


# variables to hold the locations of galaxy-free columns and rows
columns_to_expand: list[int] = []
rows_to_expand: list[int] = []

# Check each column for galaxies and if none are found append the index
# of the column to the list of columns to expand
for i in range(0, len(data[0])):
    no_galaxys: bool = check_no_galaxies(i, data)
    if no_galaxys:
        columns_to_expand.append(i)

# Check each row for galaxies and if none are found append the index
# of the column to the list of rows to expand
for i, row in enumerate(data):
    if "#" not in row:
        rows_to_expand.append(i)

# Variable to hold galaxy coordinates
galaxies: list[tuple[int, int]] = []

# loop through the rows in the data and append the x, y coordinates
# of each galaxy to the galaxies list
for i, row in enumerate(data):
    # i will hold the row index or y coordinate
    galaxies_in_row: Iterator[Match[str]] = re.finditer("#", row)
    for galaxy in galaxies_in_row:
        # .start() gives the index of the galaxy in
        # the row, ie. the x coordinate
        coordinates: tuple[int, int] = (galaxy.start(), i)
        galaxies.append(coordinates)

# variable to hold the sum of all the shortest
total_distances: int = 0

# loop through each galaxy and find the shortest distance between it
# and all of the following galaxies
for i, galaxy in enumerate(galaxies):
    for coordinates in galaxies[i + 1 :]:
        x_difference: int = abs(coordinates[0] - galaxy[0])
        # loop through the columns to expand and if they fall between the two
        # galaxies then add one to the distance
        for col in columns_to_expand:
            if min(coordinates[0], galaxy[0]) <= col <= max(coordinates[0], galaxy[0]):
                x_difference += 999999
        y_difference: int = abs(coordinates[1] - galaxy[1])
        # loop through the rows to expand and if they fall between the two
        # galaxies then add one to the distance
        for row in rows_to_expand:
            if min(coordinates[1], galaxy[1]) <= row <= max(coordinates[1], galaxy[1]):
                y_difference += 999999
        # add the X and Y differences to get the shortest
        # distance between two galaxies
        shortest_distance: int = x_difference + y_difference

        # add the distance to the total
        total_distances += shortest_distance

print(total_distances)
