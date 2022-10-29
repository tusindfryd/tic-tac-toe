"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    flat_board = [mark for row in board for mark in row]
    if flat_board.count(X) == flat_board.count(O):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    mark = player(board)
    new_board = deepcopy(board)
    field = new_board[action[0]][action[1]]
    if not field:
        new_board[action[0]][action[1]] = mark
    else:
        raise ValueError("Invalid action: field is not empty.")
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    def won_row(player):
        return any([row.count(player) == len(board) for row in board])

    def won_column(player):
        return any([row.count(player) == len(board) for row in list(zip(*board))])

    def won_diagonal(player):
        won_d1 = [board[i][i] for i in range(len(board))].count(player) == len(board)
        won_d2 = [board[i][len(board) - 1 - i] for i in range(len(board))].count(
            player
        ) == len(board)
        return won_d1 or won_d2

    def won(player):
        return won_row(player) or won_column(player) or won_diagonal(player)

    if won(X):
        return X
    elif won(O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flat_board = [mark for row in board for mark in row]
    return all(flat_board) or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(state):
        moves = actions(state)
        value = float("-inf")
        move = (None, None)

        if terminal(state):
            return utility(state), None
        for action in moves:
            move_value, _ = min_value(result(state, action))
            if move_value > value:
                value = move_value
                move = action
        return value, move

    def min_value(state):
        moves = actions(state)
        value = float("inf")
        move = (None, None)

        if terminal(state):
            return utility(state), None
        for action in moves:
            move_value, _ = max_value(result(state, action))
            if move_value < value:
                value = move_value
                move = action
        return value, move

    if player(board) == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move
