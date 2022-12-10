# Day Two
# Rock Paper Scissors game

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# If both players choose the same shape, the round instead ends in a draw.

# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# Opponent:
# A -> rock
# B -> paper
# C -> scissors

# Your move:
# X -> rock
# Y -> paper
# Z -> scissors

# sum of your scores for each round
total_score = 0

# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

shape_score = 0
outcome_score = 0
round_score = shape_score + outcome_score

def split_input(data2):

    # split each line into two separate words
    opponent_move = []
    my_move = []


    for item in data2:
        lines = item.strip().split()
        opponent_move.append(lines[0])
        my_move.append(lines[1])

    # save as new files
    # open the file in write mode
    with open('opponent.txt', 'w') as f:
        # write each element of the list on a separate line
        for item in opponent_move:
            f.write(item + '\n')
            
    with open('mymove.txt', 'w') as f:
        # write each element of the list on a separate line
        for item in my_move:
            f.write(item + '\n')

    # print the results
    print(opponent_move)
    print(my_move)

# def select_game(strategy_guide):
#
#     for item in strategy_guide:
#         game = [item[0], item[1], item[2]]
#         print(game)


if __name__ == '__main__':

    with open('data2.txt') as f:
        game = f.readlines()

    # select_game(game)
    split_input(game)

    #implementing game strategy







