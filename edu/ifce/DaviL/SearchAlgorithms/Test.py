from br.edu.ifce.DaviL.SearchAlgorithms.Agents import SimpleProblemSolvingAgent
from br.edu.ifce.DaviL.SearchAlgorithms.Problem import  RomeniaProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    problem = RomeniaProblem()
    Sequence = Agent(problem.initial_state, problem)
    print(Sequence)