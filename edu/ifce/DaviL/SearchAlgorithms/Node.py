class Node(object):
    """

    Tree Node

    """

    # Node Raiz

    #def __init__(self, parent):
    #    self.parent = None
    #    self.state = parent
    #    self.action = None

    def __init__(self, state, parent, action):

        if parent == None:
            self.state = state
            self.parent = None
            self.action = None

        if parent != None:
            self.parent = parent
            self.action = action
            self.state = state
        # self.cost = parent.cost + problem.Path_cost(parent.state, action)

    def __str__(self):
        return self.state

    def path_construct(self, node, problem):
        path = []
        while node.parent != None:
            path.append(node.state)
            node = node.parent
        path.append(node.state)
        return  path[::-1]


    def expand(self, problem, parent):
        _list = []  #
        Actions = problem.actions(parent.state)
        # print(Actions)
        for state in Actions:
            new_node = Node(state, parent, None)
            _list.append(new_node)
        return _list
