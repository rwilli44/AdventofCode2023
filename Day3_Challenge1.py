import re
from typing import Iterator, Match

# Read the input and save it as a list of strings
data: list[str] = []
with open("Data/D3_data.txt", "r") as f:
    data = f.readlines()

# var to save the result to
total: int = 0

# var to identify the current line by to allow for
# searching the previous or next line for symbols
line_index = 0
for line in data:
    # remove EOF character
    line: str = line.rstrip()

    # create a list of Match objects for every digit in the line
    numbers: Iterator[Match[str]] = re.finditer("[0-9]+", line)
    for number in numbers:
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
            # add preceeding character to the text to search
            surrounding_text += line[start_search]
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
            # add the character following the number to the text to search
            surrounding_text += line[end_digit + 1]

        # if the line is not the first in the data set, add the slice of the string
        # from the preceeding line which borders the number to the text to search
        if line_index > 0:
            surrounding_text += data[line_index - 1][start_search:end_search]

        # if the line is not the last in the data set, add the slice of the string
        # from the following line which borders the number to the text to search
        if line_index < len(data) - 1:
            surrounding_text += data[line_index + 1][start_search:end_search]

        # remove all digits and periods from the text surrounding the number to
        # leave only sumbols
        symbols: str = re.sub("[0-9]*", "", surrounding_text)
        symbols = symbols.replace(".", "")

        # if a symbol is found, add the value of the number to the total
        if len(symbols) > 0:
            total += int(number.group())
    # augment the line index before repeating the loop
    line_index += 1

# show the result
print(total)
