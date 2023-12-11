################ Data Prep ################

with open("Data/D7_data.txt", "r") as f:
    data: list[str] = f.readlines()
    games: list[str] = []
    for game in data:
        # Remove EOF character
        games.append(game.rstrip())


################ Variables ################

# List to hold dictionaries for each game with
# the count of the cards in the hand
card_counts: list[dict] = []

# Lists to contain each game of cards once it is sorted
# acording to the type of hand
five_ofa_kinds: list[dict] = []
four_ofa_kinds: list[dict] = []
full_houses: list[dict] = []
three_ofa_kind: list[dict] = []
two_pairs: list[dict] = []
one_pairs: list[dict] = []
high_cards: list[dict] = []


# Dictionary of the relative values of each card for sorting
value_dict = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "j": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

# List to store all the games in sorted order
sorted_all_games: list[str] = []

# List of the lists that contain each type of hand to
# loop through in order and add to the final sorted list
hand_types: list[list] = [
    five_ofa_kinds,
    four_ofa_kinds,
    full_houses,
    three_ofa_kind,
    two_pairs,
    one_pairs,
    high_cards,
]

# Var to store the sum of all the bet totals
total: int = 0


################ Functions ################


def count_cards(game: str) -> dict:
    """Takes a string of a card game and appends a dictionary
    to the card_counts list containing the original string and
    a key for each type of card in the and with the number of
    cards of that type as the value. Ex: 'A':3

    Args:
        game (str): A string beginnign with 5 letters/numbers
        representing a card game hand
    """
    game_dict: dict = {"game": game}

    for i in range(0, 5):
        if game[i] in game_dict.keys():
            game_dict[game[i]] = game_dict[game[i]] + 1
        else:
            game_dict[game[i]] = 1

    return game_dict


def find_game_type(game_dict) -> None:
    """Takes in a dictionary of card counts for a hand of the game
    and depending on the combination of card count the function
    appends it to the list of cards of the same type

    Args:
        game_dict (dict): a dictionary containing the
        game string and the count of each type of card
    """
    if 5 in game_dict.values():
        # if one of the values in the dictionary is 5,
        # it is a Five of a Kind hand
        five_ofa_kinds.append(game_dict["game"])

    elif 4 in game_dict.values() and game_dict.get("J", 0) == 0:
        # if one of the values in the dictionary is 4 and no joker,
        # it is a Four of a Kind hand
        four_ofa_kinds.append(game_dict["game"])

    elif 4 in game_dict.values():
        # if one of the values in the dictionary is 4 and one joker,
        # it is a Five of a Kind hand
        five_ofa_kinds.append(game_dict["game"])
    elif (
        3 in game_dict.values()
        and 2 in game_dict.values()
        and game_dict.get("J", 0) == 0
    ):
        # if two of the values in the dictionary are 3 and 2
        # and no joker, it is a Full House hand
        full_houses.append(game_dict["game"])

    elif 3 in game_dict.values() and 2 in game_dict.values():
        # if two of the values in the dictionary are 3 and 2,
        # and there are jokers it is a Five of a Kind hand
        five_ofa_kinds.append(game_dict["game"])

    elif 3 in game_dict.values() and game_dict.get("J", 0) == 0:
        # if one of the values in the dictionary is 3 and it
        # didn't have a 2 or joker, it is a Three of a Kind hand
        three_ofa_kind.append(game_dict["game"])

    elif 3 in game_dict.values():
        # if one of the values in the dictionary is 3 and it didn't
        # have a 2, but does have a joker it's a Four of a Kind hand
        four_ofa_kinds.append(game_dict["game"])

    elif len(game_dict.keys()) == 4 and game_dict.get("J", 0) == 0:
        # if the dictionary contains 4 keys and no joker, it is a Two Pairs
        # hand (a 'game' key, one key for each pair and a fifth card )
        two_pairs.append(game_dict["game"])

    elif len(game_dict.keys()) == 4 and game_dict.get("J", 0) == 1:
        # if the dictionary contains 4 keys and a joker, it is a Full House
        # hand (a 'game' key, one key for each pair and a joker)
        full_houses.append(game_dict["game"])

    elif len(game_dict.keys()) == 4 and game_dict.get("J", 0) == 2:
        # if the dictionary contains 4 keys and two jokers, it is a Four
        #  of a Kind hand (a 'game' key, one key for each pair of which one is Jokers)
        four_ofa_kinds.append(game_dict["game"])

    elif 2 in game_dict.values() and game_dict.get("J", 0) == 0:
        # if none of the previous conditions match and a key value is
        # 2 and no joker, it is a One Pair hand
        one_pairs.append(game_dict["game"])

    elif 2 in game_dict.values():
        # if none of the previous conditions match and a key value is
        # 2 and there is a joker, it is a Three of a Kind hand
        three_ofa_kind.append(game_dict["game"])

    elif game_dict.get("J", 0) == 0:
        # if none of the previous conditions match and there is no joker,
        # it is a High Card hand
        high_cards.append(game_dict["game"])

    else:
        # if none of the previous conditions match, then there are 5 different
        # cards of which one is a joker making it a One Pair hand
        one_pairs.append(game_dict["game"])


def compare_two(first_game: str, second_game: str) -> bool:
    """Returns True if the first game is of higher or equal value to the second,
    False if the second game is of higher value

    Args:
        first_game (str): a string starting with the 5 letters and numbers of a hand
        second_game (str):  a string starting with the 5 letters and numbers of a hand

    Returns:
        bool: True if the first game is of higher or equal value, False otherwise
    """
    # if the last card is a Joker, it is a tie-breaker and returns to its original value
    # position which is stored as a lower-case J, so if the final card is J it must be
    # made lowercase
    if first_game[4] == "J":
        first_game[4].lower()
    if second_game[4] == "J":
        second_game[4].lower()

    for i in range(0, 5):
        # for each card in the game, loop through to compare
        if value_dict[first_game[i]] > value_dict[second_game[i]]:
            # if a card of the first game is of higher value than the equivalent
            # card in the second, the first game is of higher value
            return True
        elif value_dict[first_game[i]] < value_dict[second_game[i]]:
            # if a card of the first game is of lower value than the equivalent
            # card in the second, the first game is of lower value
            return False
        else:
            # if both cards are equal continue the loop to compare the next card
            continue
    # if all cards are equal return false
    return False


def sort_list(original_version: list[str]) -> list[str]:
    """Takes in a list of card games and returns a list sorted
    according to the rules of the game.

    Args:
        original_version (list[str]): A list of strings in which the
        first five letters correspond to a hand of a card game

    Returns:
        list[str]: A list of strings in which the first five letters
        correspond to a hand of a card game sorted by their rank
    """
    sorted_version: list[str] = []

    # append the first game to the sorted list to begin the comparisons
    # if the following cards are of higher value they will be inserted before it,
    # otherwise they will be appended after it
    sorted_version.append(original_version[0])

    # loop through each game in the original list
    for i in range(1, len(original_version)):
        # compare it to each card in the sorted list to find
        # the right position to insert it
        for j in range(0, len(sorted_version)):
            # if the card in the sorted list is not of higher value than the
            # card it is compared to, the new card is inserted before it in
            # the sorted list
            if not compare_two(sorted_version[j], original_version[i]):
                sorted_version.insert(j, original_version[i])

                # beak the loop to begin sorting the next card
                break

            # if the card is not of higher value than any of the cards already
            # sorted it is added to the end of the sorted list
            elif j == len(sorted_version) - 1:
                sorted_version.append(original_version[i])

    return sorted_version


################ Main Section ################

# Loop through each game from the dataset and append its
# dictionary of card counts to the list
for game in games:
    game_dict: dict = count_cards(game)
    card_counts.append(game_dict)

# Loop through each dictionary of card counts to find the type
# of hand and append it to the appropriate list
for game_dict in card_counts:
    find_game_type(game_dict)


#  Loop through each list of types of hands and sort the cards by
# the ranking system described in the challenge
for hand in hand_types:
    # The if statement is not needed for the final solution, but
    # is for the test case where not every type of hand is included
    if len(hand) > 0:
        # sort the list by rank
        sorted_version = sort_list(hand)
        # add the list to the total list of all games
        sorted_all_games.extend(sorted_version)

# Reverse the list as games with the highest value have the lowest number ranking
sorted_all_games.reverse()

# Loop through the sorted list of all games, multiply their rank by their bet
# value and add it to the total
for i, game in enumerate(sorted_all_games):
    # the bet value is the second half of the game string
    bet = int(game.split()[1])
    # ranks begin at 1, so we need to add 1 to the index each time
    rank = i + 1
    # add the winnings - bet * rank - to the total
    total += bet * rank

# print the result
print(total)
