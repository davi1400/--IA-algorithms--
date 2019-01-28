from edu.ifce.DaviL.SearchAlgorithms.Search import *
from abc import abstractmethod


class SimpleProblemSolvingAgent(object):

    def __init__(self, initial_state=None):
        super(SimpleProblemSolvingAgent, self).__init__()

        self.state = initial_state
        '''
            Return an action
        '''

    @abstractmethod
    def search(self, problem):
        pass

    @abstractmethod
    def update_state(state, percept):
        """
        :param state:
        :param percept:
        :return:
        """
        pass

    @abstractmethod
    def formulate_goal(self, state):
        pass

    @abstractmethod
    def formulate_Problem(self, state, goal):
        pass


# ------------------------------------------------------------------------------------------------


class AgentAStar(SimpleProblemSolvingAgent):

    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        final_node, path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        final_node, sequence = A_Star_Search(problem)
        print final_node.state
        return final_node, sequence

    def update_state(state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentBestGreedySearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        final_node, path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        final_node, sequence = best_greedy_search(problem)
        print final_node.state
        return final_node, sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


# ------------------------------------------------------------------------------------------------


class AgentBreathFirstSearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        final_node, path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        final_node, sequence = BreathFirstSearch(problem)
        print final_node.state
        return final_node, sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentDepthFirstSearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        final_node, path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        final_node, sequence = DepthFirstSearch(problem)
        print final_node.state
        return final_node, sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentDepthFirstSearchExplored(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        final_node, path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        final_node, sequence = DepthFirstSearch_ExploredVector(problem)
        print final_node.state
        return final_node, sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentBirectionalSearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        sequence = bidirectional_search(problem)
        return sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentUnifordCostSearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        sequence = cost_uniform_search(problem)
        return sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass


class AgentIterativeDeepingSearch(SimpleProblemSolvingAgent):
    def __init__(self):
        super(SimpleProblemSolvingAgent)

    def __call__(self, percept, problem):
        path = self.search(problem)
        if path is []:
            print "Not path"
            return []
        else:
            problem.execution(path)

    def search(self, problem):
        sequence = iterative_deep_limited_search(problem)
        return sequence

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass
