from edu.ifce.DaviL.SearchAlgorithms.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.SearchAlgorithms.Problem import RomeniaProblem, EightPuzzeProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = RomeniaProblem()
    Sequence = Agent(environment.initial_state)
