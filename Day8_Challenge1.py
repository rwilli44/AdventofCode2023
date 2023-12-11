import re

# load the data
with open("Data/D8_data.txt", "r") as f:
    data: list[str] = f.readlines()

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
for line in data[2:]:
    node_data: list[str] = re.findall("[A-Z]{3}", line)
    node_map.append(node_data)

# set starting node
node: str = "AAA"
# set counter to track the position in the instructions
instruction_position: int = 0
# counter to track the number of steps
steps: int = 0

# continue until you reach "ZZZ"
while node != "ZZZ":
    # count the step
    steps += 1
    # if we have reached the end of the instructions string, start over
    if instruction_position == len(instructions):
        instruction_position = 0
    # get the integer to use for the position of the next L/R instruction to follow
    position = int(instructions[instruction_position])
    # movea  step down the instructions
    instruction_position += 1
    # loop through the map to find the matching node
    for value in node_map:
        if value[0] == node:
            # when a match is found, use the L/R position to set the value of the next
            # node to find
            node = value[position]

            # break the cycle of the loop to check if node is "ZZZ"
            break
# print the total number of steps to get to ZZZ
print(steps)
