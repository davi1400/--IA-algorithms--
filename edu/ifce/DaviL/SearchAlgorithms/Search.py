from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Queue import Queue
from collections import deque
from operator import attrgetter
from pythonds.basic.stack import Stack
import time
from numpy import where, array

'''
Search Module

'''


def BreathFirstSearch(problem):
    No = Node(problem.initial_state, None, None, 0.0)
    if problem.test_goal(No.state):
        return No.path_construct(No)

    LIFO_LIST = Queue()  # type: Queue # FIFO list
    LIFO_LIST.put(No)
    iteration = 0
    while not LIFO_LIST.empty():
        if iteration >= 1000000:
            break
        parent = LIFO_LIST.get()
        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent):
            LIFO_LIST.put(child)
        iteration += 1
    print 'Final depth %s' % (parent.depth)
    return [], []


def DepthFirstSearch(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No.path_construct(No)

    STACK_LIST = Stack()
    STACK_LIST.push(No)
    iteration = 0
    while not STACK_LIST.isEmpty():
        if iteration >= 1000000:
            break
        parent = STACK_LIST.pop()
        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent):
            STACK_LIST.push(child)
        iteration += 1
    print 'Final depth %s' % (parent.depth)
    return [], []


def DepthFirstSearch_ExploredVector(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No.path_construct(No)

    STACK_LIST = Stack()
    STACK_LIST.push(No)
    ExploredVector = []

    while not STACK_LIST.isEmpty():
        # now = datetime.datetime.now()
        parent = STACK_LIST.pop()
        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent):
            if child.state not in ExploredVector:
                STACK_LIST.push(child)
        ExploredVector.append(parent.state)

    return [], []


def BPL(problem, limit):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return True, No

    STACK_LIST = Stack()
    STACK_LIST.push(No)
    solution = True
    count = 0
    while not STACK_LIST.isEmpty():
        parent = STACK_LIST.pop()

        if parent.depth <= limit:
            if problem.test_goal(parent.state):
                return True, parent
            else:
                for child in problem.expand(parent):
                    if problem.test_goal(child.state):
                        return True, child
                    else:
                        STACK_LIST.push(child)
                        count += 1
        else:
            continue
    return [], []


def iterative_deep_limited_search(problem):
    for i in range(10000):
        boll, solution = BPL(problem, i)
        if boll:
            return solution.path_construct(solution)
        else:
            print 'dont have a solve with limit %i' % (i)


def cost_uniform_search(problem):
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No.path_construct(No)

    priority_list = deque([No])

    while priority_list.maxlen != 0:
        parent = priority_list.popleft()
        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent):  # type: object
            priority_list.append(child)
        priority_list = deque(sorted(priority_list, key=attrgetter('g')))
    print("Don't have a solve")
    return [], []


def isin(no, list_no):
    i = 0
    for i in range(list_no.maxsize):
        if (no.state == list_no[i].state):
            return True, i
    return False, i


# TODO
def path(begin, finish):
    path = []
    action=[]
    aux = begin.parent
    while aux is not None:
        path.append(aux.state)
        if(aux.parent is not None):
         action.append(aux.action)
            
        aux = aux.parent
    path = path[::-1]
    action=action[::-1]
    aux = finish.parent
    while aux is not None:
        if aux.state not in path:
            path.append(aux.state)
            if(aux.parent is not None):
                action.append(aux.action)
        aux = aux.parent
    return path


def bidirectional_search(problem):
    start = Node(problem.initial_state, None, None, None)
    goal = Node(problem.goal, None, None, None)

    start_explored = []
    goal_explored = []

    if problem.test_goal(start.state):
        return start, start.path_construct(start)

    stack_start = Queue()
    stack_goal = Queue()

    stack_start.put(start)
    stack_goal.put(goal)

    while (not (stack_goal.empty()) and not (stack_start.empty())):
        parent_start = stack_start.get()
        parent_goal = stack_goal.get()
        aux1, i = isin(parent_start, stack_goal)
        if (aux1):
            return path(parent_start, stack_goal[i]), parent_start.action

        aux1, i = isin(parent_goal, stack_start)
        if (aux1):
            return path(stack_start[i], parent_goal)

        if (parent_start.state == parent_goal.state):
            return path(parent_start, parent_goal)

        for child in problem.expand(parent_start):
            if child not in start_explored:
                stack_start.put(child)
        start_explored.append(parent_start)

        for child in problem.expand(parent_goal):
            if child not in goal_explored:
                stack_goal.put(child)
        goal_explored.append(parent_goal)

    print("Don't have a solve")
    return [], []


# ----------------------------------------------------------------------------------------------------------------------
# Heuristic search


def A_Star_Search(problem):
    """
    :type problem: object
    """
    No = Node(problem.initial_state, None, None, None)  # type: Node
    No._f_(problem.initial_state, problem)
    if problem.test_goal(No.state):
        return No.path_construct(No)

    PRIORITY_LIST = deque([No])
    # open_list = list()

    while PRIORITY_LIST.__len__() != 0:
        parent = PRIORITY_LIST.popleft()
        # open_list.append(parent.state)

        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent, True):  # type: objec
            if child.f == 0:
                child._f_(child.state, problem)
            # if child.state in open_list:
            #    continue
            # open_list.append(child.state)
            PRIORITY_LIST.append(child)
        # open_list.remove(parent.state)
        PRIORITY_LIST = deque(sorted(PRIORITY_LIST, key=attrgetter('f')))
    return [], []


def best_greedy_search(problem):
    """
        :type problem: object
        """
    No = Node(problem.initial_state, None, None, None)  # type: Node
    if problem.test_goal(No.state):
        return No.path_construct(No)

    PRIORITY_LIST = deque([No])
    # open_list = list()

    while PRIORITY_LIST.maxlen != 0:
        parent = PRIORITY_LIST.popleft()
        # open_list.append(parent.state)

        if problem.test_goal(parent.state):
            return parent.path_construct(parent)

        for child in problem.expand(parent, True):  # type: object
            # if child.state in open_list:
            #    continue
            # open_list.append(child.state)
            PRIORITY_LIST.append(child)
        # open_list.remove(parent.state)

        PRIORITY_LIST = deque(sorted(PRIORITY_LIST, key=attrgetter('h')))
    return [], []
