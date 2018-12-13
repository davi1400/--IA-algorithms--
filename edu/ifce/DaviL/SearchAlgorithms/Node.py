class Node(object):
    """

    Tree Node

    """

    # Node Raiz

    # def __init__(self, parent):
    #    self.parent = None
    #    self.state = parent
    #    self.action = None

    def __init__(self, state, parent, action, cost):

        if parent == None:
            self.state = state
            self.parent = None
            self.action = None
            self.cost = 0.0

        if parent != None:
            self.parent = parent
            self.action = action
            self.state = state
            self.cost = parent.cost + cost

    def __str__(self):
        return self.state

    def path_construct(self, node):
        path = []
        Total_cost = node.cost
        while node.parent != None:
            path.append(node.state)
            node = node.parent
        path.append(node.state)
        print 'The total cost is %d' % Total_cost
        return path[::-1]

    def expand(self, problem, parent):
        _list = []  #
        Actions = problem.actions(parent.state)
        for state in Actions:
            new_node = Node(state, parent, None, Actions[state])
            _list.append(new_node)
        return _list

    # Heuristic function for Heuristic search
    def _h_(self):
        pass

    # function that calculate the cost to Cost Uniform Search
    def _g_(self):
        pass
