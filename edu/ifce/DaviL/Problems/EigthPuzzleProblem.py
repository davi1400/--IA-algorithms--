from abc import ABCMeta

from edu.ifce.DaviL.Problems.Problem import Problem
from random import shuffle
from numpy import array, arange, reshape, where


class EightPuzzleProblem(Problem):

    def __init__(self):
        self.initial_state = arange(9)
        shuffle(self.initial_state)
        self.goal = array([0, 1, 2, 3, 4, 5, 6, 7, 8])

    def actions(self, state):
        actions = ['UP', 'DOWN', 'LEFT', 'RIGTH']
        matrix = reshape(state, (3, 3))
        i = where(matrix == 0)[0][0]
        j = where(matrix == 0)[1][0]

        if i - 1 < 0:
            actions.remove('UP')
        if i + 1 > matrix.shape[0]:
            actions.remove('DOWN')
        if j - 1 < 0:
            actions.remove('LEFT')
        if j + 1 > matrix.shape[1]:
            actions.remove('RIGTH')

        print actions
        return self.result(matrix, actions, i, j)

    def result(self, matrix, actions, i, j):
        all_actions = []
        for act in actions:
            if act is 'UP':
                aux = matrix[i - 1][j]
                matrix[i - 1][j] = matrix[i][j]
                matrix[i][j] = aux
                all_actions.append([reshape(matrix, (3, 3)), act])
            if act is 'DOWN':
                aux = matrix[i + 1][j]
                matrix[i + 1][j] = matrix[i][j]
                matrix[i][j] = aux
                all_actions.append([reshape(matrix, (3, 3)), act])
            if act is 'LEFT':
                aux = matrix[i][j - 1]
                matrix[i][j - 1] = matrix[i][j]
                matrix[i][j] = aux
                all_actions.append([reshape(matrix, (3, 3)), act])
            if act is 'RIGTH':
                aux = matrix[i][j + 1]
                matrix[i][j + 1] = matrix[i][j]
                matrix[i][j] = aux
                all_actions.append([reshape(matrix, (3, 3)), act])

        return all_actions

    def expand(self, parent):
        _list = []  #
        Actions = self.actions(parent.state)
        pass
