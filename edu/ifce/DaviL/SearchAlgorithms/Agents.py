
from br.edu.ifce.DaviL.SearchAlgorithms.Search import BreathFirstSearch, DepthFirstSearch
from br.edu.ifce.DaviL.SearchAlgorithms.Problem import RomeniaProblem


class SimpleProblemSolvingAgent(object):

    def __init__(self, initial_state=None):
        super(SimpleProblemSolvingAgent, self).__init__()

        self.state = initial_state
        '''
            Return an action
        '''

    def __call__(self, perception, problem):
        '''

        :param perception: environment perception
        :return:

        '''

        seq = []
        self.state = self.update_state(self.state, perception)
        if seq.__len__() == 0:
            # problem = self.formulate_Problem()  # type: object
            self.goal = problem.goal
            goal_test, seq = self.search(problem)
            # print(goal_test)
            # print(self.goal)
            if seq.__len__ == 0:
                return 'Not possible find'
        return seq



    def search(self, problem):
        """

        :return: an search algorithm

        """
        print('1: BreathFirstSearch')
        print('2: DepthFirstSearch')
        input = int(raw_input())
        if input == 1:
            print ('Choiced BreathFirstSearch ')
            final_node, path = BreathFirstSearch(problem)
            return final_node, path
        if input == 2:
            print ('Choiced DepthFirstSearch ')
            final_node, path = DepthFirstSearch(problem)
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
        """

        :param state:
        :return:
        """



        pass


    def formulate_problem(self):
        """

        :param state:
        :param goal:
        :return:
        """
        print('choice the problem')
        print('1 Romania Problem')
        print('2 ......')
        number_problem = raw_input()
        if number_problem is 1:
            problem = RomeniaProblem()  # type: RomeniaProblem
            return problem


