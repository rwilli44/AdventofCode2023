import re
import unittest


def get_distances(race_time: int | str) -> list[int]:
    """For a given time, find the possible distances that can be
    covered if for each second the acceleration key is held the
    boat does not move but gains 1m/sec in speed for the time it
    does spend moving. Ex: If there are 10 seconds, a boat may
    spend 1 second holding the key and 9 moving for a distance of
    9m.

    Args:
        race_time (int | str ): the time the race takes

    Returns:
        list[int]: a list of the possible distances covered excluding 0s
    """
    distances: list[int] = []
    race_time = int(race_time)
    for second in range(1, race_time):
        distances.append((race_time - second) * second)
    return distances


def find_wins(possible_distances: list[int], record_distance: int) -> int:
    """For a given list of possible distances and the record distance, find
    the number of possible distances which break the record.

    Args:
        possible_distances (list[int]): distances a boat can go in the given race
        record_distance (int): the current record distance to beat

    Returns:
        int: the number of possible distances which break the record
    """
    total_broken_records: int = 0
    for distance in possible_distances:
        if distance > record_distance:
            total_broken_records += 1
    return total_broken_records


def total_ways_to_win(possible_wins: list[int]) -> int:
    """For a list of possible ways to break the recod in a number of races,
    calculate the total number of ways to break all the records.

    Args:
        possible_wins (list[int]): a list of the number of ways to break each record

    Returns:
        int: the total number of combinations
    """
    total: int = 1
    for wins in possible_wins:
        total = wins * total
    return total


with open("D6_data.txt", "r") as f:
    # get the string of race times
    times = f.readline()
    # get the string of distance records
    distances = f.readline()
    # convert the strings into lists of just the numbers
    times = re.findall("[0-9]+", times)
    distances = re.findall("[0-9]+", distances)

# a list to store the number of ways to win for each race
possible_wins = []
for i in range(0, len(times)):
    # for each race, get the number of distances possible
    possible_distances = get_distances(times[i])
    # get the record distance for the race
    record_distance = int(distances[i])
    # find the number of wins and append it to the list of possibilities
    possible_wins.append(find_wins(possible_distances, record_distance))

# show how many combinations of ways to break the record exist
print(total_ways_to_win(possible_wins))

### TESTS FOR THE FUNCTIONS BASED ON AoC EXAMPLE DATA


class TestString(unittest.TestCase):
    def test_get_distances(self):
        time = 7
        expected_distances = [6, 10, 12, 12, 10, 6]
        self.assertEqual(get_distances(7), expected_distances)

    def test_find_wins(self):
        record_distance = 9
        possible_distances = [6, 10, 12, 12, 10, 6]
        self.assertEqual(find_wins(possible_distances, record_distance), 4)

    def test_total_ways_to_win(self):
        possible_wins = [4, 8, 9]
        expected_total = 288
        self.assertEqual(total_ways_to_win(possible_wins), expected_total)


if __name__ == "__main__":
    unittest.main()
