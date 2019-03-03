import numpy as np


def C(n):
    if n < 2:
        return 0
    return np.math.factorial(n) / (np.math.factorial(2) * np.math.factorial(n - 2))


def get_board(queens):
    Board = np.zeros((8, 8))
    for q in range(queens.__len__()):
        i = queens[q]
        Board[i][q] = 1
    return Board


def calculate_eval(queens):
    Board = get_board(queens)

    sumOflines = sum([C(sum(Board[line])) for line in range(8)])
    sumOfDiagonals = sum([C(Board.trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board.trace(offset=-diag)) for diag in range(1, 9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=-diag)) for diag in range(1, 9)])

    return sumOflines + sumOfDiagonals


def genereate_state():
    queens = np.random.randint(8, size=(8))
    return queens


def generate_temp():
    return (0.10) * np.random.rand() + 0.90


# TODO
def neighbors(currentState):  # pertuba
    state1 = currentState.copy()
    state1[np.random.randint(8, size=1)[0]] = np.random.randint(8, size=1)
    state2 = currentState.copy()
    state2[np.random.randint(8, size=1)[0]] = np.random.randint(8, size=1)

    return state1


def Board(queens):
    board = get_board(queens)
    for i in range(board.shape[0]):
        print(8 * "----")
        stri = ""
        for j in range(board.shape[1]):
            if board[i][j] == 1:
                stri += "| 1 "
            else:
                stri += "| 0 "
        print stri


if __name__ == '__main__':
    state = genereate_state()
    temperature = generate_temp()
    Max_iter = 100
    L = 50
    alpha = 0.7
    P = 200
    M = 100
    j = 1

    while True:
        i = 0
        nSucesso = 0
        while True:
            next_state = neighbors(state)
            delta_eval = calculate_eval(next_state) - calculate_eval(state)
            if (delta_eval <= 0) or (np.exp(-1.0 * delta_eval / temperature) > np.random.rand()):
                state = next_state
                nSucesso += 1
            if (nSucesso >= L) or (i > P):
                break
        if (nSucesso == 0) or (j > M):
            break
        temperature = alpha * temperature
        j += 1

    print(state)
    print(calculate_eval(state))
    print(get_board(state))
