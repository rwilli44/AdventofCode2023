import re


def checkValidity(game: list) -> bool:
    """This function takes in a list split from a game played, checks
    the quantity of each color cube against the limit, and returns true
    if it doesn't go over the limit and false if it does

    Args:
        game (list): a list split from the string describing a game

    Returns:
        bool: True if all cubes are within the quantities allowed
    """

    # Start the loop at the first color indicator in position 3
    i: int = 3

    # Row lengths are variable so continue until the end of the row
    while i <= len(game) - 1:
        # identify the color by its first letter to avoid
        # issues with punctuation at the end
        color: str = game[i][0]
        # get the quantity of cubes from the preceeding position
        quantity: int = int(game[i - 1])
        # check if the number of cubes passes the max for the given color
        match color:
            case "r":
                if quantity > 12:
                    return False
            case "g":
                if quantity > 13:
                    return False
            case "b":
                if quantity > 14:
                    return False
        # increment counter
        i += 2
    # if all tests pass return true
    return True


SUM: int = 0

with open("Data/D2_data.txt", "r") as f:
    games: list = f.readlines()
    for line in games:
        # split each row into a list
        game: list = line.split()

        # pass the list to the function and if it returns true
        # add the game ID to the total
        if checkValidity(game):
            game_id: int = int(game[1][:-1])
            SUM += game_id
print(SUM)
