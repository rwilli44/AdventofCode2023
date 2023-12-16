import re

with open("Data/D8_data.txt", "r") as f:
    data = f.readlines()


# remove EOF character from line 1, which is the instructions for the map
instructions: str = data[0].strip()

# for moves to the "right" ina  row we will be looking at the node
# in the 3rd position of our list, so we'll change R to index 2
# to allow for easily selecting the right node and similarly 1 for L
instructions = instructions.replace("R", "2")
instructions = instructions.replace("L", "1")

# list to hold lists made up of each node and its left/right instructions
node_map: list[list[str]] = []
# loop through each row of data to extract just the node/instructions
for i, line in enumerate(data[2:]):
    node_data: list[str] = re.findall("[A-Z0-9]{3}", line)
    node_with_index = [i, node_data]
    node_map.append(node_with_index)

# list to store all of the nodes starting with all the AAAs
nodes = []
first_instruction = int(instructions[0])
for line in node_map:
    line_nodes = line[1]
    first_node = line_nodes[0]
    last_letter = first_node[2]
    if last_letter == "A":
        nodes.append([line[0], line_nodes[first_instruction]])

# set counter to track the position in the instructions
instruction_position: int = 1
# counter to track the number of steps
steps: int = 1

steps_get_to_Z = [0, 0, 0, 0, 0, 0]

not_all_Zs = True
# continue until you reach "ZZZ"
while not_all_Zs:
    # count the step
    steps += 1
    # if we have reached the end of the instructions string, start over
    if instruction_position == len(instructions):
        instruction_position = 0
    # get the integer to use for the position of the next L/R instruction to follow
    L_or_R = int(instructions[instruction_position])

    # move a  step down the instructions for the next turn
    instruction_position += 1

    # loop through the map to find the matching node
    for i, node in enumerate(nodes):
        # get the position of the current node in the original map to make sure you search forward
        starting_position = node[0]
        # get the value you need to match in the original map
        node_value = node[1]
        # loop through the original map to find the matching node
        match_found = False
        for row in node_map[starting_position:]:
            # check that the position of the original node is before the position being tested
            # if the value of the left position in the map is the same as the node we are searching for,
            # update it in nodes
            row_nodes = row[1]

            if row_nodes[0] == node_value:
                new_node = row_nodes[L_or_R]
                pos = row[0]
                add_to_nodes = [pos, new_node]
                nodes[i] = add_to_nodes
                match_found = True
                break

        if not match_found:
            for row in node_map[:starting_position]:
                row_nodes = row[1]
                if row_nodes[0] == node_value:
                    new_node = row_nodes[L_or_R]
                    pos = row[0]
                    add_to_nodes = [pos, new_node]
                    nodes[i] = add_to_nodes
                    break

    count_Zs = 0
    for i, node in enumerate(nodes):
        if node[1][2] == "Z" and steps_get_to_Z[i] == 0:
            steps_get_to_Z[i] = steps
    if 0 not in steps_get_to_Z:
        not_all_Zs = False
        # print the total number of steps to get to ZZZ
        print(steps_get_to_Z)

find_lcm = max(steps_get_to_Z)
steps_get_to_Z.sort(reverse=True)
total_divisible = 0

while total_divisible < len(steps_get_to_Z):
    total_divisible = 0
    for number in steps_get_to_Z:
        if find_lcm % number != 0:
            find_lcm += max(steps_get_to_Z)
            break
        else:
            total_divisible += 1
print(find_lcm)
