class Node(object):
    """
    Tree Node
    """

    # Node Raiz

    # def __init__(self, parent):
    #    self.parent = None
    #    self.state = parent
    #    self.action = None

    def __init__(self, state, parent, action, path_cost=None, heuristic=None):

        if parent == None:
            self.state = state
            self.parent = None
            self.action = None
            self.path_cost = 0.0
            self.f = 0
            self.h = heuristic
            self.depth = 0
            self.g = self.path_cost

        if parent != None:
            self.parent = parent
            self.action = action
            self.state = state
            self.depth = parent.depth + 1
            self.path_cost = path_cost
            self.f = 0
            self.h = heuristic
            self.g = self.path_cost

    def __str__(self):
        return self.state

    def path_construct(self, node):
        path = []
        act = []
        Total_cost = node.path_cost
        while node.parent is not None:
            path.append(node.state)
            act.append(node.action)
            node = node.parent
        path.append(node.state)
        act.append(node.action)
        print 'The total cost is %d' % Total_cost
        return path[::-1], act[::-1]

    # Heuristic function for Heuristic search
    def _h_(self, state, problem):
        return problem.heuristic(state)

    # function that calculate the cost to Cost Uniform Search
    def _g_(self):
        return self.path_cost

    def _f_(self, state, problem):
        self.f += int((self._h_(state, problem) + self._g_()))
        return

    def get_cost(self):
        return self.path_cost
