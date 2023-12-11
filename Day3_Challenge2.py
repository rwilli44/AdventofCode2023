import re
from typing import Iterator, Match


# function to test if a character is a symbol
def isSymbol(char: str) -> bool:
    """Test if a character is a symbol (excluding .)
    Args:
        char (str): a one character string

    Returns:
        bool: True if the char is a symbol, False otherwise
    """
    if not char.isdigit() and char != ".":
        return True
    else:
        return False


# Read the input and save it as a list of strings
data: list[str] = []
with open("Data/D3_data.txt", "r") as f:
    data = f.readlines()

# var to save the result to
total: int = 0

# var to save number values and symbol location pairs to
# format [number_value, (x,y)] where x = index of the sumbol
# in the line and y = the index of the line
numb_symbol_locs: list[list[int | tuple[int, int]]] = []

# var to save a list of unique locations where a symbol borders a number
unique_locations = set()

# var to identify the current line by to allow for
# searching the previous or next line for symbols
line_index = 0

for line in data:
    # remove EOF character
    line: str = line.rstrip()

    # create a list of Match objects for every digit in the line
    numbers: Iterator[Match[str]] = re.finditer("[0-9]+", line)

    for number in numbers:
        # int value of the number
        number_value: int = int(number.group())
        # index of the first digit in the number
        start_digit: int = number.start()
        # index of the last digit in the number
        end_digit: int = number.end() - 1
        # string to store all of the text surrounding the number
        surrounding_text: str = ""
        # set the start index from which to search for symbols
        if start_digit > 0:
            # if the digit isn't at the start of the line,
            # search will start one index position back
            start_search: int = start_digit - 1

            # test preceeding character for a symbol
            if isSymbol(line[start_search]):
                loc: tuple[int, int] = (start_search, line_index)
                value_symbol: list[int | tuple[int, int]] = [number_value, loc]
                numb_symbol_locs.append(value_symbol)
                unique_locations.add(loc)

        else:
            # if the digit is at the start of the line, set the
            # index to begin searching at to 0 for searching the lines
            # above and below
            start_search: int = 0

        # Set the index for where the search could end. Because a slice does
        # not include the last index number, this is 2 places beyond the end
        # of the number so that the character following the number is included
        # in the slice
        if number.end() == len(line):
            # if the number is at the end of the line, set the index for the end
            # of the search to the length of the line
            end_search: int = len(line)
        else:
            # otherwise set the end point to two after the index of the last digit
            # in the number so that the character followign it is included in the
            # search
            end_search: int = end_digit + 2

            # test preceeding character for a symbol
            if isSymbol(line[end_digit + 1]):
                loc: tuple[int, int] = (end_digit + 1, line_index)
                value_symbol: list[int | tuple[int, int]] = [number_value, loc]

                # if a symbol is found, add to the list of numbers
                # and locations as well as the list of unique locations
                numb_symbol_locs.append(value_symbol)
                unique_locations.add(loc)

        # if the line is not the first in the data set, add the slice of the string
        # from the preceeding line which borders the number to the text to search
        if line_index > 0:
            # var to save the position in the slice to be able to find the index
            # of the character in the line should a symbol be found
            i_in_slice: int = 0
            slice_prev_line: str = data[line_index - 1][start_search:end_search]
            for character in slice_prev_line:
                # test each character in the slice to see if it is a symbol
                if isSymbol(character):
                    loc: tuple[int, int] = (start_search + i_in_slice, line_index - 1)
                    value_symbol: list[int | tuple[int, int]] = [
                        number_value,
                        loc,
                    ]

                    # if a symbol is found, add to the list of numbers
                    # and locations as well as the list of unique locations
                    numb_symbol_locs.append(value_symbol)
                    unique_locations.add(loc)
                # increase index position
                i_in_slice += 1

        # if the line is not the last in the data set, add the slice of the string
        # from the following line which borders the number to the text to search
        if line_index < len(data) - 1:
            # var to save the position in the slice to be able to find the index
            # of the character in the line should a symbol be found
            i_in_slice: int = 0
            slice_next_line: str = data[line_index + 1][start_search:end_search]
            for character in slice_next_line:
                # test each character in the slice to see if it is a symbol
                if isSymbol(character):
                    loc: tuple[int, int] = (start_search + i_in_slice, line_index + 1)
                    value_symbol: list[int | tuple[int, int]] = [
                        number_value,
                        loc,
                    ]

                    # if a symbol is found, add to the list of numbers
                    # and locations as well as the list of unique locations
                    numb_symbol_locs.append(value_symbol)
                    unique_locations.add(loc)
                # increase index position
                i_in_slice += 1

    # increase the line index before repeating the loop
    line_index += 1

# for each unique symbol location bordering a nubmer,
# search for all appearances in the complete list of numbers
# and if there are 2 the corresponding numbers are multiplied
# and added to the total
for loc in unique_locations:
    # store the number each time the location is found in the list
    numbers_used: list = []
    for number in numb_symbol_locs:
        # save the number if the location is found
        if number[1] == loc:
            numbers_used.append(number[0])
    # if two numbers are found, the result of their muliplication
    # is added to the total
    if len(numbers_used) == 2:
        multiplied_value: int = numbers_used[0] * numbers_used[1]
        total += multiplied_value

# show the result
print(total)
