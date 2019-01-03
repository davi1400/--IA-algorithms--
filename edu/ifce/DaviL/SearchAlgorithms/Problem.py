from abc import abstractmethod
from random import choice
from numpy import array, where, reshape
from random import shuffle
from edu.ifce.DaviL.Utils.EightPuzzleEnum import EightPuzzleEnum


class Problem(object):
    """
        Abstract class
    """
    goal = None  # type: object

    def __init__(self, initial_state, goal=None):
        super(Problem, self).__init__()
        self.initial_state = initial_state
        self.goal = goal

    @abstractmethod
    def actions(self, state):
        return NotImplementedError

    @abstractmethod
    def result(self, state, action):
        return NotImplementedError

    def test_goal(self, state):
        return state == self.goal

    @abstractmethod
    def get_goal(self):
        return self.goal

    @abstractmethod
    def path_cost(self, c, state1, state2):
        return c + 1


class EightPuzzleProblem(Problem):
    def get_goal(self):
        pass

    def __init__(self):
        self.magic_matrix = array([[1, 2, 3],
                                   [4, 0, 6],
                                   [7, 8, 5]])
        for i in range(self.magic_matrix.shape[0]):
            shuffle(self.magic_matrix[i])

        i = where(self.magic_matrix == 0)[0][0]
        j = where(self.magic_matrix == 0)[1][0]
        self.initial_state = (i, j)
        self.n = 3  # line
        self.m = 3  # column
        self.goal = array([[0, 1, 2],
                           [3, 4, 5],
                           [6, 7, 8]])

    def actions(self, state):
        # state is a tuple (i,j)
        # i = state[0] and j = state[1]

        # diagonal
        if state == (0, self.m - 1):
            print 1
            return self.result(state, EightPuzzleEnum.DOWN), self.result(state, EightPuzzleEnum.RIGHT)
        elif state == (self.n - 1, self.m - 1):
            print 2
            return self.result(state, EightPuzzleEnum.UP), self.result(state, EightPuzzleEnum.RIGHT)
        elif state == (0, 0):
            print 3
            return self.result(state, EightPuzzleEnum.DOWN), self.result(state, EightPuzzleEnum.LEFT)
        elif state == (self.n - 1, 0):
            print 4
            return self.result(state, EightPuzzleEnum.UP), self.result(state, EightPuzzleEnum.LEFT)

        # between line or column
        elif state[0] == 0 and (state[1] != 0 and state[1] != self.m - 1):
            print 5
            return self.result(state, EightPuzzleEnum.LEFT), self.result(state, EightPuzzleEnum.RIGHT), \
                   self.result(state, EightPuzzleEnum.DOWN)
        elif state[0] == self.n - 1 and (state[1] != 0 and state[1] != self.m - 1):
            print 6
            return self.result(state, EightPuzzleEnum.LEFT), self.result(state, EightPuzzleEnum.RIGHT), \
                   self.result(state, EightPuzzleEnum.UP)
        elif state[1] == 0 and (state[0] != 0 and state[0] != self.n - 1):
            print 7
            return self.result(state, EightPuzzleEnum.UP), self.result(state, EightPuzzleEnum.DOWN), \
                   self.result(state, EightPuzzleEnum.LEFT)
        elif state[1] == self.m - 1 and (state[0] != 0 and state[0] != self.n - 1):
            print 8
            return self.result(state, EightPuzzleEnum.UP), self.result(state, EightPuzzleEnum.DOWN), \
                   self.result(state, EightPuzzleEnum.RIGHT)

        else:
            print 9
            return self.result(state, EightPuzzleEnum.UP), self.result(state, EightPuzzleEnum.DOWN), \
                   self.result(state, EightPuzzleEnum.RIGHT), self.result(state, EightPuzzleEnum.LEFT)

    def result(self, state, action):
        i = state[0]
        j = state[1]
        if action == EightPuzzleEnum.LEFT:
            print 'left'
            magic = self.magic_matrix.copy()
            state_now = magic[i][j + 1]
            magic[i][j + 1] = magic[i][j]
            magic[i][j] = state_now
            magic_list = reshape(magic, 9).tolist()
            return {(i, j + 1): magic_list}, EightPuzzleEnum.LEFT
        elif action == EightPuzzleEnum.RIGHT:
            print 'right'
            magic = self.magic_matrix.copy()
            state_now = magic[i][j - 1]
            magic[i][j - 1] = magic[i][j]
            magic[i][j] = state_now
            magic_list = reshape(magic, 9).tolist()
            return {(i, j - 1): magic_list}, EightPuzzleEnum.RIGHT
        elif action == EightPuzzleEnum.UP:
            print 'up'
            magic = self.magic_matrix.copy()
            state_now = magic[i - 1][j]
            magic[i - 1][j] = magic[i][j]
            magic[i][j] = state_now
            magic_list = reshape(magic, 9).tolist()
            return {(i - 1, j): magic_list}, EightPuzzleEnum.UP
        elif action == EightPuzzleEnum.DOWN:
            print 'down'
            magic = self.magic_matrix.copy()
            state_now = magic[i + 1][j]
            magic[i + 1][j] = magic[i][j]
            magic[i][j] = state_now
            magic_list = reshape(magic, 9).tolist()
            return {(i + 1, j): magic_list}, EightPuzzleEnum.DOWN

    def test_goal(self, state):
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.magic_matrix[i][j] != count:
                    return False
                count += 1
        return True

    def path_cost(self, c, state1, state2):
        pass

    def heuristic(self, state):
        return 0


class RomeniaProblem(Problem):
    def __init__(self):
        # type: () -> object
        super(Problem, self).__init__()
        self.initial_state = 'arad'
        self.goal = 'bucharest'

    # TODO
    def actions(self, state):

        """
        :param state:
        :return: the actions of a state
        """
        actions = {
            'arad': {'zerind': 75, 'sibiu': 140, 'timisoara': 118},
            'zerind': {'arad': 75, 'oradea': 71},
            'timisoara': {'arad': 118, 'lugoj': 111},
            'bucharest': {'urziceni': 85, 'pitesti': 101, 'giurgiu': 90, 'fagaras': 211},
            'craiovoa': {'drobeta': 120, 'rimmicu vilcea': 146, 'pitesti': 138},
            'drobeta': {'mehadia': 75, 'craiovoa': 120},
            'eforie': {'hirsova': 86},
            'fagaras': {'sibiu': 99, 'bucharest': 211},
            'hirsova': {'urziceni': 98, 'eforie': 86},
            'iasi': {'vaslui': 92, 'neamt': 87},
            'lugoj': {'timisoara': 111, 'mehadia': 70},
            'oradea': {'zerind': 71, 'sibiu': 151},
            'pitesti': {'rimmicu vilcea': 97, 'craiovoa': 138, 'bucharest': 101},
            'urziceni': {'vaslui': 142, 'bucharest': 85, 'hirsova': 98},
            'neamt': {'iasi': 87},
            'vaslui': {'iasi': 92, 'urziceni': 142},
            'giurgiu': {'bucharest': 90},
            'rimmicu vilcea': {'sibiu': 99, 'pitesti': 97, 'craiovoa': 146},
            'sibiu': {'fagaras': 99, 'rimmicu vilcea': 80, 'arad': 140, 'oradea': 151},
            'mehadia': {'lugoj': 70, 'drobeta': 75}
        }

        return actions[state]

    def result(self, state, action):
        """
        :param state:
        :param action:
        :return:  Result in a new state of the problem given an action
        """

        if action is not None:
            actions = self.actions(state)
            next_state, value = choice(list(actions.items()))
            return next_state
        return state

    def get_goal(self):
        return self.goal

    def path_cost(self, c, state1, state2):
        return c + self.actions(state1)[state2]

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print 'Estado atual %s ir para %s' % (path[next_action], path[next_action + 1])

        print 'Chegou em %s' % (path[len(path) - 1])

    def heuristic(self, state):

        H = {'arad': 366,
             'bucharest': 0,
             'craiovoa': 160,
             'drobeta': 242,
             'eforie': 161,
             'fagaras': 176,
             'giurgiu': 77,
             'hirsova': 151,
             'iasi': 226,
             'lugoj': 244,
             'mehadia': 241,
             'neamt': 234,
             'oradea': 380,
             'pitesti': 101,
             'rimmicu vilcea': 193,
             'sibiu': 253,
             'timisoara': 329,
             'urziceni': 80,
             'vaslui': 193,
             'zerind': 374
             }

        return H[state]
