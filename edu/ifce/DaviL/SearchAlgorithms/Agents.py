from edu.ifce.DaviL.SearchAlgorithms.Search import *
from edu.ifce.DaviL.SearchAlgorithms.Problem import RomeniaProblem


class SimpleProblemSolvingAgent(object):

    def __init__(self, initial_state=None):
        super(SimpleProblemSolvingAgent, self).__init__()

        self.state = initial_state
        '''
            Return an action
        '''

    def __call__(self, perception, problem):
        """
        :param perception: environment perception
        :return:
        """

        seq = []
        self.state = self.update_state(self.state, perception)
        if seq.__len__() == 0:

            self.goal = problem.goal
            problem = problem  # type: object
            goal_test, seq = self.search(problem)
            if seq.__len__ == 0:
                return 'Not possible find'
        return problem.execution(seq)

    def search(self, problem):
        """
        :return: an search algorithm
        """
        print('1: BreathFirstSearch')
        print('2: DepthFirstSearch')
        print('3: DepthFirstSearch with Explored Vector')
        print('4: A_Star_Search')
        print('5: best_greedy_search')
        input = int(raw_input())
        if input == 1:
            print ('Choiced BreathFirstSearch ')
            final_node, path = BreathFirstSearch(problem)
            return final_node, path
        if input == 2:
            print ('Choiced DepthFirstSearch ')
            final_node, path = DepthFirstSearch(problem)
            return final_node, path
        if input == 3:
            print ('Choiced DepthFirstSearch with Explored Vector ')
            final_node, path = DepthFirstSearch_ExploredVector(problem)
            return final_node, path
        if input == 4:
            print ('Coiced A_Star_Search')
            final_node, path = A_Star_Search(problem)
            return final_node, path
        if input == 5:
            print ('Coiced best_greedy_search')
            final_node, path = best_greedy_search(problem)
            return final_node, path

    @staticmethod
    def update_state(state, percept):
        """
        :param state:
        :param percept:
        :return:
        """
        state = percept
        return state

    def formulate_goal(self, state):
        # type: (object) -> object
        """
        :param state:
        :return:
        """
        goal = 'bucharest'
        return goal

    def formulate_Problem(self, state, goal):
        """
        :param state:
        :param goal:
        :return:
        """

        # print('choice the problem')
        # print('1 Romania Problem')
        # print('2 ......')
        # number_problem = int(raw_input())
        # if number_problem is 1:
        problem = RomeniaProblem()  # type: RomeniaProblem
        return problem