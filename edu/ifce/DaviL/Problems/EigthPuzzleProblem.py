from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from edu.ifce.DaviL.Problems.Problem import Problem
from random import shuffle
from numpy import array, arange, reshape, where


class EightPuzzleProblem(Problem):

    def __init__(self):
        self.initial_state = arange(9).tolist()
        shuffle(self.initial_state)
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def actions(self, state):
        actions = ['UP', 'DOWN', 'LEFT', 'RIGTH']
        matrix = reshape(state, (3, 3))
        i = where(matrix == 0)[0][0]
        j = where(matrix == 0)[1][0]

        if i - 1 < 0:
            actions.remove('UP')
        if i + 1 > matrix.shape[0] - 1:
            actions.remove('DOWN')
        if j - 1 < 0:
            actions.remove('LEFT')
        if j + 1 > matrix.shape[1] - 1:
            actions.remove('RIGTH')

        return self.result(matrix, actions, i, j)

    def result(self, matrix, actions, i, j):
        all_actions = []
        for act in actions:
            if act is 'UP':
                matrix_ = matrix.copy()
                aux = matrix_[i - 1][j]
                matrix_[i - 1][j] = matrix_[i][j]
                matrix_[i][j] = aux
                all_actions.append([reshape(matrix_, 9).tolist(), act])
            if act is 'DOWN':
                matrix_ = matrix.copy()
                aux = matrix_[i + 1][j]
                matrix_[i + 1][j] = matrix_[i][j]
                matrix_[i][j] = aux
                all_actions.append([reshape(matrix_, 9).tolist(), act])
            if act is 'LEFT':
                matrix_ = matrix.copy()
                aux = matrix_[i][j - 1]
                matrix_[i][j - 1] = matrix_[i][j]
                matrix_[i][j] = aux
                all_actions.append([reshape(matrix_, 9).tolist(), act])
            if act is 'RIGTH':
                matrix_ = matrix.copy()
                aux = matrix_[i][j + 1]
                matrix_[i][j + 1] = matrix_[i][j]
                matrix_[i][j] = aux
                all_actions.append([reshape(matrix_, 9).tolist(), act])

        return all_actions

    def expand(self, parent):
        _list = []  #
        for state, act in self.actions(parent.state):
            new_node = Node(state, parent, act, self.path_cost(parent.path_cost, parent.state, state), self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return c + 1

    def heuristic(self, state):
        h = 0
        for i in range(len(state)):
            if state[i] != self.goal[i]:
                h += 1
        return h

    def test_goal(self, state):
        if state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return True
        return False

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print reshape(path[next_action], (3, 3))
        print reshape(path[len(path) - 1], (3, 3))
        return