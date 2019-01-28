from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from edu.ifce.DaviL.Problems.Problem import Problem
from random import shuffle
from numpy import array, arange, reshape, where
from numpy.random import randint


class EightPuzzleProblem(Problem):

    def __init__(self, random_moves, initial_state= None):
        if initial_state is None:
            self.initial_state = self.generate(random_moves)
            while not self.isSolvable():
                self.initial_state = self.generate(random_moves)
        else:
            self.initial_state = initial_state
        # random_moves = randint(100)
        # for moves in range(random_moves):
        #    i_random = randint(len(self.initial_state))
        #    i_zero = where(array(self.initial_state) == 0)[0][0]
        #    aux = self.initial_state[i_random]
        #    self.initial_state[i_random] = self.initial_state[i_zero]
        #    self.initial_state[i_zero] = aux
        # print random_moves
        print reshape(self.initial_state, (3, 3))
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        # self.Visited_nodes = [self.initial_state]
        self.explored = []

    def isSolvable(self):
        count = 0
        for i in range(len(self.initial_state)):
            for j in range(i + 1, len(self.initial_state)):
                if self.initial_state[i] > self.initial_state[j] and self.initial_state[j] != 0:
                    count += 1
        return count % 2 == 0

    def generate(self, random_moves):
        self.initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        for i_random in range(random_moves):
            j_random = randint(len(self.initial_state))
            i_zero = where(array(self.initial_state) == 0)[0][0]
            aux = self.initial_state[j_random]
            self.initial_state[j_random] = self.initial_state[i_zero]
            self.initial_state[i_zero] = aux
        return self.initial_state

    def actions(self, state):
        actions = ['UP', 'DOWN', 'LEFT', 'RIGTH']
        i = where(array(state) == 0)[0][0]
        length = len(state) - 1

        if i - 3 < 0:
            actions.remove('UP')
        if i + 3 > length:
            actions.remove('DOWN')
        if i % 3 == 0:
            actions.remove('LEFT')
        if (i + 1) % 3 == 0:
            actions.remove('RIGTH')

        return self.result(state, actions, i)

    def result(self, state, actions, i):
        all_actions = []
        for act in actions:
            if act is 'UP':
                aux_state = array(state).tolist()
                aux = aux_state[i - 3]
                aux_state[i - 3] = aux_state[i]
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
        _list = []
        # self.Visited_nodes.append(parent.state)
        for state, act in self.actions(parent.state):
            # if state not in self.Visited_nodes:
            new_node = Node(state, parent, act, self.path_cost(parent.path_cost, parent.state, state),
                            self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
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
                value = matrix[i][j]
                if value != 0:
                    # targetX = (value - 1) / matrix.shape[0]
                    # targetY = (value - 1) % matrix.shape[0]
                    # dx = i - targetX
                    # dy = j - targetY
                    X = [i, j]
                    Y = [where(matrix_goal == matrix[i][j])[0][0], where(matrix_goal == matrix[i][j])[1][0]]
                    Manhattan_distance += sum(abs(array(X) - array(Y)))
                    # Manhattan_distance += (abs(dx) + abs(dy))
        return Manhattan_distance

    def heuristic1(self, state):
        # Using Haming distance
        distance = 0
        for i in range(len(state)):
            if state[i] != self.goal[i] and state[i] != 0:
                distance += 1
        return distance

    def test_goal(self, state):
        if state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            return True
        return False

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print reshape(path[next_action], (3, 3))
        print reshape(path[len(path) - 1], (3, 3))
        return path
