from br.edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Queue import Queue, LifoQueue

'''
Search Module
'''


def BreathFirstSearch(problem):
    No = Node(problem.initial_state, None, None, 0.0)
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    FIFO_LIST = Queue()  # type: Queue # FIFO list
    FIFO_LIST.put(No)

    # VISITED_NODES = []

    while not FIFO_LIST.empty():
        parent = FIFO_LIST.get()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in parent.expand(problem, parent):
            FIFO_LIST.put(child)


def DepthFirstSearch(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    LIFO_LIST = LifoQueue()
    LIFO_LIST.put(No)

    while not LIFO_LIST.empty():
        parent = LIFO_LIST.get()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in parent.expand(problem, parent):
            LIFO_LIST.put(child)


def DepthFirstSearch_ExploredVector(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    LIFO_LIST = LifoQueue()
    LIFO_LIST.put(No)
    ExploredVector = []

    while not LIFO_LIST.empty():
        parent = LIFO_LIST.get()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in parent.expand(problem, parent):
            if child.state not in ExploredVector:
                LIFO_LIST.put(child)
                print(child)
        ExploredVector.append(parent.state)