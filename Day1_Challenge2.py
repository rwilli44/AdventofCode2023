# Constants to use for substring search
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
NUMBER_STRINGS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


sum = 0

with open("Data/D1_data.txt", "r") as f:
    calibration_data = f.readlines()
    for line in calibration_data:
        # Remove EOF characters
        line = line.rstrip()

        # Position of the first and last number in the line
        # Set arbitrarily high so that they are replaced
        # with correct values after the first loop
        pos_first = 10000
        post_last = 10000

        # The value of the first and last number in the string
        # Will be converted to int at the end after they are concatenated
        first_value = ""
        last_value = ""

        # These bools let us indicate if the first or last number found
        # is a word to allow us to convert it to a single digit at the end
        first_is_word = False
        last_is_word = False

        for numb in DIGITS:
            # Compare index of first appearance of the number to the lowest
            # index already found. If it is lower but not -1, set the number
            # as the first value and reset the position of the lowest number found
            first_index = line.find(numb)
            if first_index < pos_first and first_index >= 0:
                pos_first = first_index
                first_value = numb
                first_is_word = False

            # Reverse the line to search for the last digit used using the same
            # Method used above
            last_index = line[::-1].find(numb)
            if last_index < post_last and last_index >= 0:
                post_last = last_index
                last_value = numb
                last_is_word = False

        for numb in NUMBER_STRINGS:
            # Compare index of first appearance of the word to the lowest
            # index already found. If it is lower but not -1, set the word
            # as the first value and reset the position of the lowest number found
            # Also set first_is_word to True
            first_index = line.find(numb)
            if first_index < pos_first and first_index >= 0:
                pos_first = first_index
                first_value = numb
                first_is_word = True

            # Reverse the line to search for the last digit used using the same
            # Method used above. The number word must also be reversed.
            last_index = line[::-1].find(numb[::-1])
            if last_index < post_last and last_index >= 0:
                post_last = last_index
                last_value = numb
                last_is_word = True

        # If the first or last number found in the string is in the form of a word,
        # convert it to a string of a single digit for the concatenation by finding
        # its index in the NUMBER_STRINGS list and adding 1 (ex: "one" is at index 0)
        if last_is_word:
            last_value = str(NUMBER_STRINGS.index(last_value) + 1)
        if first_is_word:
            first_value = str(NUMBER_STRINGS.index(first_value) + 1)

        # Concatenate the first and last digit and convert it to an integer
        coordinate = int(first_value + last_value)

        # Add the integer to the sum
        sum += coordinate

# Show the result
print(sum)
