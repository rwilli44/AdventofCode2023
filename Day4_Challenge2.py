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


# Stores the input as rows of two lists of strings
data: list[list[str]] = []

with open("D4_data.txt", "r") as f:
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

# store the number of matches found for each row of
matches_per_row: list[int] = []
for row in data:
    number_matches = find_matches(row[1], row[0])
    matches_per_row.append(number_matches)

# create a list to store the number of scratchcards each row has
# starting with one per row
number_cards_per_row: list[int] = [1 for number in range(0, len(data))]

total_scratchards = 0
row_index = 0

for row_index in range(0, len(data)):
    # for each row of scratchcards, add the number of cards to the total
    total_scratchards += number_cards_per_row[row_index]
    # for each match in the row, loop through to increase the number of
    # cards in the following rows
    for j in range(1, matches_per_row[row_index] + 1):
        # for each copy of the game card, add one card to the count for the row j
        # rows after the game card
        number_cards_per_row[row_index + j] += number_cards_per_row[row_index]

# show result
print(total_scratchards)
