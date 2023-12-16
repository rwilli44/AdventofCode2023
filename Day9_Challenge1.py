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
    total_row = 0
    for row in final_matrices:
        total_row = row[-1] + total_row

    return total_row


overall_total = 0

for row in data:
    overall_total += find_total(row)

print(overall_total)
