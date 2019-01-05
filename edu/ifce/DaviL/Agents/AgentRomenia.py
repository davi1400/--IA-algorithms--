from edu.ifce.DaviL.Agents.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.Problems.RomeniaProblem import RomeniaProblem
if __name__ == '__main__':
    Agent = SimpleProblemSolvingAgent()
    environment = RomeniaProblem()
    sequence = Sequence = Agent(environment.initial_state, environment)
