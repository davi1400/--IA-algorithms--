from numpy.random import shuffle
class Node(object):
    """
    Tree Node
    """

    # Node Raiz

    # def __init__(self, parent):
    #    self.parent = None
    #    self.state = parent
    #    self.action = None

    def __init__(self, state, parent, action, cost, heuristic=None):

        if parent == None:
            self.state = state
            self.parent = None
            self.action = None
            self.cost = 0.0
            self.f = 0
            self.h = heuristic

        if parent != None:
            self.parent = parent
            self.action = action
            self.state = state
            self.cost = parent.cost + cost
            self.f = 0
            self.h = heuristic

    def __str__(self):
        return self.state

    def path_construct(self, node):
        path = []
        Total_cost = node.cost
        while node.parent is not None:
            path.append(node.state)
            node = node.parent
        path.append(node.state)
        print 'The total cost is %d' % Total_cost
        return path[::-1]

    def expand(self, problem, parent):
        _list = []  #
        Actions = problem.actions(parent.state)
        for state in Actions:
            new_node = Node(state, parent, None, Actions[state], self._h_(state, problem))
            _list.append(new_node)
        shuffle(_list)
        return _list

    # Heuristic function for Heuristic search
    def _h_(self, state, problem):
        return problem.heuristic(state)

    # function that calculate the cost to Cost Uniform Search
    def _g_(self):
        return self.cost

    def _f_(self, state, problem):
        self.f += int((self._h_(state, problem) + self._g_()))
        return

    def get_cost(self):
        return self.cost
