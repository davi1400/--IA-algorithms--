from edu.ifce.DaviL.SearchAlgorithms.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.SearchAlgorithms.Problem import RomeniaProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = RomeniaProblem()
    sequence = Sequence = Agent(environment.initial_state, environment)
