from edu.ifce.DaviL.Agents.Agents import SimpleProblemSolvingAgent
from edu.ifce.DaviL.Problems.RomeniaProblem import RomeniaProblem
import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    Agent = SimpleProblemSolvingAgent()
    environment = RomeniaProblem()
    sequence = Sequence = Agent(environment.initial_state, environment)
    final = datetime.datetime.now()
    print " Total time:"
    print (final - now)