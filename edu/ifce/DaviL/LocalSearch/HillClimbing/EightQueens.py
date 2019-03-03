"""
    Eight queens problem solved by hill climbing original algorithm and hill climbing with a stochastic method
    that generate the initial state several times and pick best final state.
"""

import numpy as np
from operator import itemgetter


def C(n):
    if n < 2:
        return 0
    return np.math.factorial(n) / (np.math.factorial(2) * np.math.factorial(n - 2))


def calculate_eval(queens):
    Board = np.zeros((8, 8))
    for q in range(queens.__len__()):
        i = queens[q]
        Board[i][q] = 1

    sumOflines = sum([C(sum(Board[line])) for line in range(8)])
    sumOfDiagonals = sum([C(Board.trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board.trace(offset=-diag)) for diag in range(1, 9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=diag)) for diag in range(9)])
    sumOfDiagonals += sum([C(Board[::-1].trace(offset=-diag)) for diag in range(1, 9)])

    return sumOflines + sumOfDiagonals


def genereate_state():
    queens = np.random.randint(8, size=(8))
    return queens


# TODO
def neighbors(currentState):
    s = []
    for i in range(2):
        state1 = currentState.copy()
        state1[np.random.randint(8, size=1)[0]] = np.random.randint(8, size=1)
        s.append(state1)

    return s


if __name__ == '__main__':
    # using hill climbing algorithm for minimiun attack in the board
    state = genereate_state()

    while True:
        n = neighbors(state)
        next_eval = 999
        next_state = None

        for neighbor in n:
            if calculate_eval(neighbor) < next_eval:
                next_eval = calculate_eval(neighbor)
                next_state = neighbor

        if next_eval >= calculate_eval(state):
            break
        if next_state is not None:
            state = next_state
    print('the best one is: ', next_eval)

    # using an stochastic method for minumun local problem
    All_Best_states = {}

    for i in range(7):
        state = genereate_state()
        while True:
            n = neighbors(state)
            next_eval = 999
            next_state = None

            for neighbor in n:
                if calculate_eval(neighbor) < next_eval:
                    next_eval = calculate_eval(neighbor)
                    next_state = neighbor

            if next_eval >= calculate_eval(state):
                break
            if next_state is not None:
                state = next_state
        All_Best_states.update({next_eval: next_state})

    print("The best state is", All_Best_states[min(All_Best_states.keys())], 'with ', min(All_Best_states.keys()),
          "attacks")
