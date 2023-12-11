import re

# Functions for today's challenge
"""

    Args:
        line (list[list[str]]): A row of the data converted into a list of
        winning numbers and a list of scratch card numbers nested in one list.
    Returns:
        int: an integer value of of the total number of matches
    """


def find_matches(scratch_card: list[str], winning_numbers: list[str]) -> int:
    """Takes two lists of strings and counts the number of elements in the second list
    (scratch_card) which can be found in the first (winning_numbers).

    Args:
        scratch_card (list[str]): the game card numbers
        winning_numbers (list[str]): the winning numbers

    Returns:
        int: the total number of matches
    """
    number_matches: int = 0
    for number in scratch_card:
        if number in winning_numbers:
            number_matches += 1
    return number_matches


def calculate_points(number_matches: int) -> int:
    """Calculate points where the first match is worth 1 point
    and every subsequent match doubles the number of points.

    Args:
        number_matches (int): number of matches found

    Returns:
        int: total number of points
    """
    if number_matches > 0:
        return 2 ** (number_matches - 1)
    else:
        return 0


# Stores the input as rows of two lists of strings
data: list[list[str]] = []

with open("Data/D4_data.txt", "r") as f:
    file_contents = f.readlines()
    for line in file_contents:
        # Remove the Game number info from the string
        line = re.sub(".*:", "", line)
        # Split into two lists of numbers
        line = line.split("|")
        # list to store the two sub-lists of winning
        # numbers and game numbers
        split_data = []
        for section in line:
            # remove EOF character
            section = section.strip()
            # split string into individual numbers
            section = section.split(" ")
            # keep only numbers and not spaces
            section = [number for number in section if number.isdigit()]
            # add the cleaned up data to the split_data list
            split_data.append(section)
        # add the cleaned up data to the data var
        data.append(split_data)

# use the find_matches and calculate_points functions to find
# the score for each row and add it to the total
total = 0
points_per_row: list[int] = []
for row in data:
    number_matches = find_matches(row[1], row[0])
    total += calculate_points(number_matches)

# show result
print(total)
