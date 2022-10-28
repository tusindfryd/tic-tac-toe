"""
Tic Tac Toe Player
"""

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
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    mark = player(board)
    new_board = board
    new_board[action[0]][action[1]] = mark
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if not terminal(board):
        return None

    def won_row(player, board):
        return any([row.count(player) == len(board) ** 0.5 for row in board])

    def won_column(player, board):
        return any(
            [row.count(player) == len(board) ** 0.5 for row in list(zip(*board))]
        )

    def won_diagonal(player, board):
        won_d1 = [board[i][i] for i in range(len(board))].count(player) == len(
            board
        ) ** 0.5
        won_d2 = [board[i][len(board) - 1 - i] for i in range(len(board))].count(
            player
        ) == len(board) ** 0.5
        return won_d1 or won_d2

    def won(player, board=board):
        return won_row(player) or won_column(player) or won_diagonal(player)

    if won(X):
        return X
    if won(O):
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flat_board = [mark for row in board for mark in row]

    if flat_board.count(EMPTY) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
