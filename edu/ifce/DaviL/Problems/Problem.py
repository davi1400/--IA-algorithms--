from abc import abstractmethod


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
        # type: (object, object) -> object
        """

        :rtype: object
        """
        # type: (object, object) -> object
        return NotImplementedError

    def test_goal(self, state):
        return state == self.goal

    @abstractmethod
    def get_goal(self):
        return self.goal

    @abstractmethod
    def path_cost(self, c, state1, state2):
        return c + 1
