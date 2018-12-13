from br.edu.ifce.DaviL.SearchAlgorithms.Agents import SimpleProblemSolvingAgent
from br.edu.ifce.DaviL.SearchAlgorithms.Problem import  RomeniaProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = RomeniaProblem('arad', 'bucharest')
    Sequence = Agent(environment.initial_state)
