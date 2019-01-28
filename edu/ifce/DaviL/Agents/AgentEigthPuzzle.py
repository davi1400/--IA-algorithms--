from edu.ifce.DaviL.Agents.Agents import *
from edu.ifce.DaviL.Problems.EigthPuzzleProblem import EightPuzzleProblem
import time
from numpy import  reshape

if __name__ == '__main__':
    Realizacoes = 20
    Total = 0
    hits = 0
    avg_time = 0
    '''
    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    print 'Agente de busca A estrela com 20 realizacoes'
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentAStar()
        environment = EightPuzzleProblem(100)
        print  'number of random moves %s' % (environment)
        if environment.isSolvable():
            print('is Solvable')
            Total += 1
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1

        else:
            print 'not solvable'
        end = time.time()
        print 'total time in %s seconds' % (end - now)
        avg_time += (end - now)
        print "---------------------------------------------------"
    print 'average time is %s seconds' % (avg_time / 20.0)

    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    hits = 0
    avg_time = 0
    print 'Agente de busca pela melhor escolha com 20 realizacoes'
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBestGreedySearch()
        environment = EightPuzzleProblem(100)
        if environment.isSolvable():
            print('is Solvable')
            Total += 1
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1

        else:
            print 'not solvable'
        end = time.time()
        print 'total time in %s seconds' % (end - now)
        avg_time += (end - now)
        print "---------------------------------------------------"
    print 'average time is %s seconds' % (avg_time / 20.0)
    '''
    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    hits = 0
    avg_time = 0
    print 'Agente de busca em largura com 20 realizacoes'
    Tests = [
        array([[0, 1, 3],
               [4, 2, 5],
               [7, 8, 6]]),
        array([[1, 3, 5],
               [7, 4, 6],
               [0, 2, 8]]),
        array([[4, 1, 3],
               [2, 0, 8],
               [7, 6, 5]]),
        array([[0, 4, 6],
               [5, 3, 1],
               [2, 7, 8]]),
        array([[3, 6, 8],
               [1, 2, 5],
               [4, 7, 0]])

    ]
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBreathFirstSearch()
        environment = EightPuzzleProblem(3, reshape(Tests[i], 9).tolist())
        if environment.isSolvable():
            print('is Solvable')
            Total += 1
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1

        else:
            print 'not solvable'
        end = time.time()
        print 'total time in %s seconds' % (end - now)
        avg_time += (end - now)
        print "---------------------------------------------------"
    print 'average time is %s seconds' % (avg_time / 20.0)


    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    hits = 0
    avg_time = 0
    print 'Agente de busca iterativa com 20 realizacoes'
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentIterativeDeepingSearch()
        environment = EightPuzzleProblem(15)
        if environment.isSolvable():
            print('is Solvable')
            Total += 1
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1

        else:
            print 'not solvable'
        end = time.time()
        print 'total time in %s seconds' % (end - now)
        avg_time += (end - now)
        print "---------------------------------------------------"
    print 'average time is %s seconds' % (avg_time / 20.0)
