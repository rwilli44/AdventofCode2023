import re

with open("Data/D1_data.txt", "r") as f:
    calibration_data = f.readlines()
    sum = 0
    for line in calibration_data:
        # remove EOF character
        line = line.rstrip()
        # remove letters
        pattern = "[A-Za-z]"
        line = re.sub(pattern, "", line)

        # combine first and last digit and add to sum
        sum += int(line[0] + line[-1])

    print(sum)
