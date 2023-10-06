letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
          5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# combine letters and points with added blank tiles as 0.
letters_to_points = {letter: point for letter, point in zip(letters, points)}
letters_to_points[" "] = 0
print(letters_to_points)


# Score a word.
def score_word(word):
    # return the total score of each letter in the word.
    # for example passed in word: brownie => Score: 15.
    point_total = 0
    for letter in word:
        point_total += letters_to_points[letter]

    return point_total


brownie_points = score_word("BROWNIE")
print(brownie_points)

# Score a game
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}


def update_point_totals():
    # Loop through the words that the players input and calculate the total point.
    # Then, push the players and their points into player_to_points.
    for player, words in player_to_words.items():
        player_points = 0
        for w in words:
            player_points += score_word(w)

        player_to_points[player] = player_points


# Add a player and the words they plays
def play_word(player_name, word):
    # if this is a new player.
    if player_name not in player_to_words.keys():
        played_words = [word]
        player_to_words[player_name] = played_words
    else:
        player_to_words[player_name].append(word)


play_word("Bao", "Python")
play_word("Bao", "JAVA")
play_word("Bao", "Love")

update_point_totals()
print(player_to_points)
