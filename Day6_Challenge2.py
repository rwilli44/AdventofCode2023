import re


def get_distances(race_time: int | str, record_time: int) -> int:
    """For a given time, find the number of possible distances that can
    be covered if for each second the acceleration key is held the
    boat does not move but gains 1m/sec in speed for the time it
    does spend moving. Ex: If there are 10 seconds, a boat may
    spend 1 second holding the key and 9 moving for a distance of
    9m.

    Args:
        race_time (int | str ): the time the race takes

    Returns:
        list[int]: a list of the possible distances covered excluding 0s
    """
    distances: int = 0
    race_time = int(race_time)
    for second in range(1, race_time):
        if ((race_time - second) * second) > record_time:
            distances += 1
    return distances


with open("D6_data.txt", "r") as f:
    # get the string for the race time
    times = f.readline()
    # get the string of distance record
    distances = f.readline()
    # convert the strings into lists of just the numbers
    times = re.findall("[0-9]+", times)
    distances = re.findall("[0-9]+", distances)
    # concatenate the strings to get the race time
    race_time = ""
    for number in times:
        race_time += number
    # concatenate the strings to get the record distance
    record_distance = ""
    for number in distances:
        record_distance += number

# show the number of possible ways to beat the record distance
print(get_distances(race_time, int(record_distance)))
