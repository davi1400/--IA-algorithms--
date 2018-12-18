from br.edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Queue import Queue, LifoQueue, PriorityQueue

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


# ----------------------------------------------------------------------------------------------------------------------
# Heuristic search


def A_Star_Search(problem):
    """

    :type problem: object
    """
    No = Node(problem.initial_state, None, None, None)  # type: Node
    No._f_(problem.initial_state, problem)
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    PRIORITY_LIST = PriorityQueue('min')
    PRIORITY_LIST.put(No)
    list_ = list()

    while not PRIORITY_LIST.empty():
        parent = PRIORITY_LIST.get()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in parent.expand(problem, parent):  # type: object
            if child.f != 0:
                child._f_(child.state, problem)
            list_.append(child)
            list_.sort(child.f)
        for elements in list_:
            PRIORITY_LIST.put(elements)

