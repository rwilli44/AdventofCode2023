import re


def seed_map(seed: int, map: list[list[int]]) -> int:
    """The function takes in a map where the first digit is the Destination start, the second is the
    Source start, and the 3rd is the length of the plot. If the seed falls within the range  o fone
    of the plots in the map, its new value is computed and returned. Otherwise the seed's original
    value is returned.

    Args:
        seed (int): the number to transform
        map (list[list[int]]): the plot describing how the number may transform

    Returns:
        int: the result of the mapping of the seed number
    """
    # check each line in the map for the seed value
    for row in map:
        # assure all variables are ints
        destination_start: int = row[0]
        source_start: int = row[1]
        map_length: int = row[2]
        # if the seed value is in the line's range, calculate and return the new value
        if seed >= source_start and seed < (source_start + map_length):
            result = destination_start + (seed - source_start)
            return result
    # if the seed value is not in the ranges of the map, return the original value
    return seed


# maps will hold lists of lists to match the original multi-demensional arrays
maps = [[], [], [], [], [], [], []]
seeds = []

# Load and prep the data
with open("Data/D5_data.txt", "r") as f:
    data = f.readlines()

    # pattern to remove most text from the data leaving only '-- ' to identify where a map change occurs
    pattern = "[A-Za-z:]"
    # index to keep track of which map or seed data is being read
    i = 0
    for line in data:
        # remove EOF
        line = line.rstrip()
        # remove most text
        line = re.sub(pattern, "", line)
        # filter so that empty strings and dashes are not included in the maps
        if len(line) > 0 and "-- " not in line:
            # if the line is only numbers and spaces, seperate the numbers into a list
            number_list = re.findall("[0-9]+", line)
            # convert all string numbers to ints
            number_list = [int(x) for x in number_list]
            # the first line is seeds insert it into the front of the map list to avoid
            # nesting lists in lists unnecessarily
            if i == 0:
                seeds = number_list
            else:
                # otherwise append the list to its map in the list of maps
                maps[i - 1].append(number_list)
        # if the line has '--' it marks a change in map, so we need to increase the index
        # of the maps list to start a new map
        if "-- " in line:
            i += 1


# min_seed set ridiculously high so that it is replaced at the first comparison
min_seed = 1_000_000_000

# loop through each range of seeds
for i in range(0, len(seeds), 2):
    first_seed = seeds[i]
    last_seed = first_seed + seeds[i + 1]

    # the program is obscenely slow so this print allows us to show
    # some progress each time a new range of seeds starts
    print(i, " : ", first_seed)

    # loop through each seed within the given range
    for j in range(first_seed, last_seed):
        current_seed = j
        # loop through all the maps in order
        for map in maps:
            current_seed = seed_map(current_seed, map)
        # compare the result to the current lowest and if it is lower
        # reset the min_seed variable to hold the new lowest vlaue
        if current_seed < min_seed:
            min_seed = current_seed

# print the lowest value in seeds at the end of the calculations
print(min_seed)
