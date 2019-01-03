from edu.ifce.DaviL.SearchAlgorithms.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.SearchAlgorithms.Problem import EightPuzzleProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = EightPuzzleProblem()
    sequence = Sequence = Agent(environment.initial_state, environment)