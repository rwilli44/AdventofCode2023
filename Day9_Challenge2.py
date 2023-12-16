# Read the input and save it as a list of strings
data: list[str] = []
with open("Data/D9_data.txt") as f:
    data = f.readlines()


def find_total(line):
    line = line.split()
    for i, number in enumerate(line):
        number = int(number)
        line[i] = number

    all_zeros = False
    final_matrices = [line]
    while not all_zeros:
        next_row = []
        for i, numb in enumerate(line):
            if i == len(line) - 1:
                break
            difference = line[i + 1] - numb
            next_row.append(difference)
        final_matrices.append(next_row)
        number_of_zeros = 0
        for number in next_row:
            if number != 0:
                break
            else:
                number_of_zeros += 1
        line = next_row
        if number_of_zeros == len(next_row):
            all_zeros = True

    final_matrices.reverse()
    extrapolated_value = final_matrices[1][0]

    for i, row in enumerate(final_matrices):
        if i < 1 or i == len(final_matrices) - 1:
            continue
        test = final_matrices[i + 1][0]
        extrapolated_value = test - extrapolated_value

    return extrapolated_value


overall_total = 0

for row in data:
    result = find_total(row)
    overall_total += result

print(overall_total)
