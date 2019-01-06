from edu.ifce.DaviL.Agents.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.Problems.EigthPuzzleProblem import EightPuzzleProblem
import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    Agent = SimpleProblemSolvingAgent()
    environment = EightPuzzleProblem()
    sequence = Agent(environment.initial_state, environment)
    end = datetime.datetime.now()
    print end - now