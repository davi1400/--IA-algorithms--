from br.edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Queue import Queue

'''
Search Module
'''
def BreathFirstSearch(problem):
    No = Node(problem.initial_state, None, None)
    if problem.test_goal(No.state):
        return No, No.Path_construct(No, problem)

    FIFO_LIST = Queue()  # type: Queue # FIFO list
    FIFO_LIST.put(No)

    # VISITED_NODES = []

    while not FIFO_LIST.empty():
        parent = FIFO_LIST.get()
        if problem.test_goal(parent.state):
            print(parent.state)
            return parent, parent.path_construct(parent, problem)

        for child in parent.expand(problem, parent):
            FIFO_LIST.put(child)

def DepthFirstSearch(problem):
    No = Node(problem.initial_state, None, None)
