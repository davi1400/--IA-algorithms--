from edu.ifce.DaviL.Agents.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.Problems.EigthPuzzleProblem import EightPuzzleProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = EightPuzzleProblem()
    sequence = Agent(environment.initial_state, environment)