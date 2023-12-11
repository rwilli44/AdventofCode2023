import re


def findMinNeeded(game: list) -> int:
    """This function will take in a list split from the string describing one game,
    find the maximum number of each color of cubes needed, and return the "power"
    of the game which AOC defines as the minimum number of each color needed
    multiplied together

    Args:
        game (list): split from a string describing the game

    Returns:
        int: the "power" of the game
    """
    # Lists to store the quantity of cubes drawn in each color
    greens = []
    reds = []
    blues = []
    # Start the loop at the first color indicator in position 3
    i: int = 3

    # Row lengths are variable so continue until the end of the row
    while i <= len(game) - 1:
        # identify the color by its first letter to avoid
        # issues with punctuation at the end
        color: str = game[i][0]
        # get the quantity of cubes from the preceeding position
        quantity: int = int(game[i - 1])
        # Add the quantity to the correct color list
        match color:
            case "r":
                reds.append(quantity)
            case "g":
                greens.append(quantity)
            case "b":
                blues.append(quantity)

        # increment counter
        i += 2

    # return the "power" of the game ie. the
    # min number of each color needed multiplied together
    return max(reds) * max(blues) * max(greens)


SUM: int = 0

with open("Data/D2_data.txt", "r") as f:
    games: list = f.readlines()
    for line in games:
        # split each row into a list
        game: list = line.split()

        # pass the list to the function and add the
        # returned power to the toal
        SUM += findMinNeeded(game)

# show the result
print(SUM)
