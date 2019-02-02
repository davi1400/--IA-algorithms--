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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = A_Star_Search(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = best_greedy_search(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = BreathFirstSearch(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = DepthFirstSearch(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = DepthFirstSearch_ExploredVector(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = bidirectional_search(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            problem.execution(path, acts)

    def search(self, problem):
        path, acts = cost_uniform_search(problem)
        return path, acts

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
        path, acts = self.search(problem)
        if not path:
            print "Not path"
            return []
        else:
            return problem.execution(path, acts)

    def search(self, problem):
        path, acts = iterative_deep_limited_search(problem)
        return path, acts

    def update_state(self, state, percept):
        pass

    def formulate_goal(self, state):
        pass

    def formulate_Problem(self, state, goal):
        pass
