import re
import pprint

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


def expand_columns(column_index: int, star_map: list[str]) -> None:
    """Adds an extra galaxy-free column to the map at the given index.
    Args:
        column_index (int): _description_
        star_map (list[str]): _description_
    """
    for index, row in enumerate(star_map):
        # insert a new copy of each row with using concatenationg to
        # add a . at the given column index
        star_map[index] = row[: column_index + 1] + "." + row[column_index + 1 :]


# variables to hold the locations of galaxy-free columns and rows
columns_to_expand = []
rows_to_expand = []

# Check each column for galaxies and if none are found append the index
# of the column to the list of columns to expand
for i in range(0, len(data[0])):
    no_galaxys = check_no_galaxies(i, data)
    if no_galaxys:
        columns_to_expand.append(i)

# Check each row for galaxies and if none are found append the index
# of the column to the list of rows to expand
for i, row in enumerate(data):
    if "#" not in row:
        rows_to_expand.append(i)

# For each column to expand, pass the index and the map to the
# expand_columns function
for i in columns_to_expand:
    expand_columns(i, data)

# Insert an extra for for each index in the rows_to_expand list
for i in rows_to_expand:
    row_to_add = "." * len(data[0])
    data.insert(i + 1, row_to_add)

# Variable to hold galaxy coordinates
galaxies = []
for i, row in enumerate(data):
    galaxies_in_row = re.finditer("#", row)
    for galaxy in galaxies_in_row:
        coordinates = (galaxy.start(), i)
        galaxies.append(coordinates)

total_distances = 0
for i, galaxy in enumerate(galaxies):
    if i == len(galaxies) - 1:
        continue
    for coordinates in galaxies[i + 1 :]:
        x_difference = abs(coordinates[0] - galaxy[0])
        y_difference = abs(coordinates[1] - galaxy[1])
        shortest_distance = x_difference + y_difference
        if x_difference == 1:
            shortest_distance = shortest_distance - 1
        if y_difference == 1:
            shortest_distance = shortest_distance - 1
        # if coordinates[0] == 0 or galaxy[0] == 0:
        #     shortest_distance = shortest_distance - 1
        # if coordinates[1] == 0 or galaxy[1] == 0:
        #     shortest_distance = shortest_distance - 1

        print(i, shortest_distance)
        total_distances += shortest_distance

print(galaxies)
pprint.pprint(data)
