from edu.ifce.DaviL.Agents.Agents import *
from edu.ifce.DaviL.Problems.EigthPuzzleProblem import EightPuzzleProblem
import time

if __name__ == '__main__':
    Realizacoes = 10
    Total = 0

    list_of_agents = [AgentAStar(), AgentBestGreedySearch(), AgentBreathFirstSearch(), AgentDepthFirstSearch(), AgentDepthFirstSearchExplored(), AgentIterativeDeepingSearch(),
                      AgentUnifordCostSearch(), AgentBirectionalSearch()]
    names_of_agents = ['A estrela', 'melhor busca', 'largura', 'profundidade', 'profundidadade com visitados', 'profundidade iterativa', 'custo uniforme', 'bidirecional']

    j = 0
    for Agent in (list_of_agents):

        hits = 0
        avg_time = 0
        arq = open('result8puzzle.txt', 'w')
        print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        print 'Agente de busca %s com 10 realizacoes' % (names_of_agents[j])
        arq.write('+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        arq.write('Agente de busca %s com 10 realizacoes\n' % (names_of_agents[j]))
        for i in range(Realizacoes):
            print "---------------------------------------------------"
            now = time.time()
            environment = EightPuzzleProblem(30)
            print 'number of random moves %s' % (environment)
            if environment.isSolvable():
                print('is Solvable')
                Total += 1
                sequence = Agent(environment.initial_state, environment)
                if sequence:
                    hits += 1

            else:
                print 'not solvable'
            end = time.time()
            print 'total time in %s seconds' % (end - now)

            avg_time += (end - now)
            print "---------------------------------------------------"
        print 'average time is %s seconds' % (avg_time / 10.0)
        print 'Acurracy %f' % (hits/10.0)
        arq.write('average time is %s seconds\n' % (avg_time / 10.0))
        arq.write('Acurracy %f\n' % (hits/10.0))
        j += 1
        arq.close()
    '''
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

    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    hits = 0
    avg_time = 0
    print 'Agente de busca em largura com 20 realizacoes'

    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBreathFirstSearch()
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


    print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
    hits = 0
    avg_time = 0
    print 'Agente de busca iterativa com 20 realizacoes'
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentIterativeDeepingSearch()
        environment = EightPuzzleProblem(30)
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
