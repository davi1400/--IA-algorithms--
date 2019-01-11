from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from edu.ifce.DaviL.Problems.Problem import Problem
from random import shuffle
from numpy import array, arange, reshape, where


class EightPuzzleProblem(Problem):

    def __init__(self):
        self.initial_state = [2, 3, 7, 5, 4, 8, 0, 6, 1]
        # shuffle(self.initial_state)
        print reshape(self.initial_state, (3, 3))
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def actions(self, state):
        actions = ['UP', 'DOWN', 'LEFT', 'RIGTH']
        i = where(array(state) == 0)[0][0]
        length = len(state)-1

        if i-3 < 0:
            actions.remove('UP')
        if i+3 > length:
            actions.remove('DOWN')
        if i-1 < 0 or i % 3 == 0:
            actions.remove('LEFT')
        if i+1 > length or (i+1) % 3 == 0:
            actions.remove('RIGTH')

        return self.result(state, actions, i)

    def result(self, state, actions, i):
        all_actions = []
        for act in actions:
            if act is 'UP':
                aux_state = array(state).tolist()
                aux = aux_state[i-3]
                aux_state[i-3] = aux_state[i]
                aux_state[i] = aux
                all_actions.append([aux_state, act])
            if act is 'DOWN':
                aux_state = array(state).tolist()
                aux = aux_state[i + 3]
                aux_state[i + 3] = aux_state[i]
                aux_state[i] = aux
                all_actions.append([aux_state, act])
            if act is 'LEFT':
                aux_state = array(state).tolist()
                aux = aux_state[i - 1]
                aux_state[i - 1] = aux_state[i]
                aux_state[i] = aux
                all_actions.append([aux_state, act])
            if act is 'RIGTH':
                aux_state = array(state).tolist()
                aux = aux_state[i + 1]
                aux_state[i + 1] = aux_state[i]
                aux_state[i] = aux
                all_actions.append([aux_state, act])

        return all_actions

    def expand(self, parent):
        _list = []  #
        for state, act in self.actions(parent.state):
            new_node = Node(state, parent, act, self.path_cost(parent.path_cost, parent.state, state), self.heuristic(state))
            _list.append(new_node)
        # shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return c + 1

    def heuristic(self, state):
        # Using Manhattan distance
        Manhattan_distance = 0
        matrix = reshape(state, (3, 3))
        matrix_goal = reshape(self.goal, (3, 3))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                X = [i, j]
                Y = [where(matrix_goal == matrix[i][j])[0][0], where(matrix_goal == matrix[i][j])[1][0]]
                Manhattan_distance += sum(abs(array(X)-array(Y)))
        return Manhattan_distance

    def test_goal(self, state):
        if state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return True
        return False

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print reshape(path[next_action], (3, 3))
        print reshape(path[len(path) - 1], (3, 3))
        return