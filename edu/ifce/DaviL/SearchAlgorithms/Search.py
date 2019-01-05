from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Queue import Queue
from collections import deque
from operator import attrgetter
from pythonds.basic.stack import Stack

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

        for child in problem.expand(parent):
            FIFO_LIST.put(child)


def DepthFirstSearch(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    STACK_LIST = Stack()
    STACK_LIST.push(No)

    while not STACK_LIST.isEmpty():
        parent = STACK_LIST.pop()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in problem.expand(parent):
            STACK_LIST.push(child)


def DepthFirstSearch_ExploredVector(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    STACK_LIST = Stack()
    STACK_LIST.push(No)
    ExploredVector = []

    while not STACK_LIST.isEmpty():
        parent = STACK_LIST.pop()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in problem.expand(parent):
            print child.state
            if child.state not in ExploredVector:
                STACK_LIST.push(child)
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

    PRIORITY_LIST = deque([No])

    while PRIORITY_LIST.maxlen != 0:
        parent = PRIORITY_LIST.popleft()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in problem.expand(parent):  # type: object
            if child.f == 0:
                child._f_(child.state, problem)
            PRIORITY_LIST.append(child)
        PRIORITY_LIST = deque(sorted(PRIORITY_LIST, key=attrgetter('f')))


def best_greedy_search(problem):
    """
        :type problem: object
        """
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No, No.path_construct(No)

    PRIORITY_LIST = deque([No])

    while PRIORITY_LIST.maxlen != 0:
        parent = PRIORITY_LIST.popleft()
        if problem.test_goal(parent.state):
            return parent, parent.path_construct(parent)

        for child in problem.expand(parent):  # type: object
            PRIORITY_LIST.append(child)
        PRIORITY_LIST = deque(sorted(PRIORITY_LIST, key=attrgetter('h')))
