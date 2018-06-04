"""
    Tic Tac Toe AI using Minimax algorithm.
    Based on https://goo.gl/SenUmq.
    Repository: https://github.com/ardabbour/tic-tac-toe.
"""


def minimax(board, player):
    """Minimax function for playing Tic Tac Toe"""

    # Store the indexes of unused cells
    free = find_empty_cells(board)

    # End recursion if we reached the terminal state
    game_over, score = terminal_state(board, free)
    if game_over:
        return score

    # Begin recursion. This is where things get messy.
    moves = []
    for i in free:
        move = {"index": None, "score": None}
        move["index"] = i

        if player == AI_PLAYER:
            result = minimax(board, HUMAN_PLAYER)
        else:
            result = minimax(board, AI_PLAYER)

        move["score"] = result["score"]
        moves.append(move)

    if player == AI_PLAYER:
        best_score = -10000
        for i in moves:
            if i["score"] > best_score:
                best_score = i["score"]
                best_move = i
    else:
        best_score = 10000
        for i in moves:
            if i["score"] < best_score:
                best_score = i["score"]
                best_move = i

    return best_move


def terminal_state(board, free):
    """Checks if the terminal state was reached and returns the score."""

    # Default values; these will change if the terminal state is reached
    game_over = False
    score = None

    # Human wins
    if won(board, HUMAN_PLAYER):
        game_over = True
        score = -10

    # AI wins
    elif won(board, AI_PLAYER):
        game_over = True
        score = 10

    # AI ties with human
    elif not free:
        game_over = True
        score = 0

    return game_over, score


def won(board, player):
    """Determines if the player won the game."""

    cond1 = board[0] == player and board[1] == player and board[2] == player
    cond2 = board[3] == player and board[4] == player and board[5] == player
    cond3 = board[6] == player and board[7] == player and board[8] == player
    cond4 = board[0] == player and board[3] == player and board[6] == player
    cond5 = board[1] == player and board[4] == player and board[7] == player
    cond6 = board[2] == player and board[5] == player and board[8] == player
    cond7 = board[0] == player and board[4] == player and board[8] == player
    cond8 = board[2] == player and board[4] == player and board[6] == player

    if cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8:
        return True
    return False


def find_empty_cells(board):
    """Returns the empty cells of the board."""

    return [x for x in board if x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]


def check_game_status(board):
    """Checks if the game is over."""

    for i in board:
        if i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            return False
    return True


def print_board(board):
    """Print the current status of the board."""

    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("---------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("---------")
    print("{} | {} | {}".format(board[6], board[7], board[8]))


def human_turn(board, human_player):
    """Human plays their turn."""

    valid = False
    empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not valid:
        human_choice = int(input("Where would you like to play?"))
        if board[human_choice] in empty:
            valid = True
        else:
            print("The cell you chose is occupied.")
    board[human_choice] = human_player
    print_board(board)

    return board


def ai_turn(board, ai_player):
    """AI plays their turn."""

    ai_choice = minimax(board, ai_player)
    board[ai_choice["result"]] = ai_player
    print_board(board)

    return board


def main():
    """Start the game"""

    # Decide who is "x" and who is "o"
    global HUMAN_PLAYER
    global AI_PLAYER
    HUMAN_PLAYER = "a"
    while HUMAN_PLAYER.lower() not in ["x", "o"]:
        HUMAN_PLAYER = input("Choose your symbol.")
    AI_PLAYER = "x"
    if HUMAN_PLAYER == AI_PLAYER:
        AI_PLAYER = "o"

    # Decide who starts first
    first = "a"
    while first.lower() not in ["yes", "no", "y", "n"]:
        first = input("Would you like to start first?")

    # Begin game
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_over = False

    if first in ["yes", "y"]:
        board = human_turn(board, HUMAN_PLAYER)
        while not game_over:
            board = ai_turn(board, AI_PLAYER)
            board = human_turn(board, HUMAN_PLAYER)
            game_over = check_game_status(board)
    else:
        board = ai_turn(board, HUMAN_PLAYER)
        while not game_over:
            board = human_turn(board, HUMAN_PLAYER)
            board = ai_turn(board, AI_PLAYER)
            game_over = check_game_status(board)


if __name__ == "__main__":
    main()
