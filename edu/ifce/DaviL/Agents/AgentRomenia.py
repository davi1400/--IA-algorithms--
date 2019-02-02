from edu.ifce.DaviL.Agents.Agents import *
from edu.ifce.DaviL.Problems.RomeniaProblem import RomeniaProblem
import time

if __name__ == '__main__':
    Realizacoes = 10
    Total = 0

    list_of_agents = [AgentBreathFirstSearch(), AgentDepthFirstSearch(), AgentDepthFirstSearchExplored(), AgentIterativeDeepingSearch(),
                      AgentUnifordCostSearch(), AgentBirectionalSearch(), AgentAStar(), AgentBestGreedySearch()]
    names_of_agents = ['largura', 'profundidade', 'profundidadade com visitados', 'profundidade iterativa', 'custo uniforme', 'bidirecional'
                       , 'A estrela', 'melhor busca']
    arq = open('Resultados.txt', 'w')
    j = 0
    for Agent in (list_of_agents):

        hits = 0
        avg_time = 0
        print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        print 'Agente de busca %s com 10 realizacoes' % (names_of_agents[j])
        arq.write('+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        arq.write('Agente de busca %s com 10 realizacoes\n' % (names_of_agents[j]))
        for i in range(Realizacoes):
            print "---------------------------------------------------"
            now = time.time()
            environment = RomeniaProblem()
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1
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
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca pela melhor escolha com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca pela melhor escolha com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBestGreedySearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"

    # Non- heuristic search
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca em largura com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca em largura com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBreathFirstSearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"

    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca em profundidade com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca em profundidade com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentDepthFirstSearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"

    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca em profundidade com lista de visitados com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca em profundidade com lista de visitados com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentDepthFirstSearchExplored()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"
    fim = time.time()
    print (fim - inicio)

    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca em profundidade iterativa com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca em profundidade iterativa com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentIterativeDeepingSearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"
    fim = time.time()
    print (fim - inicio)

    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca bidirecional com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca bidirecional com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentBirectionalSearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"

    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print 'Agente de busca custo uniforme com 20 realizacoes'
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca custo uniforme com 20 realizacoes\n')
    hits = 0
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentUnifordCostSearch()
        environment = RomeniaProblem()
        print '%s To %s' % (environment.initial_state, environment.goal)
        sequence = Agent(environment.initial_state, environment)
        if sequence != []:
            hits += 1
        end = time.time()
    print 'total time in %s seconds' % (end - now)
    media_time += (end - now)
    print 'media time %f' % (media_time / 20.0)
    arq.write('media time %.15f\n' % (media_time / 20.0))
    print 'Acuracy %f' % (hits / 20.0)
    arq.write('Acuracy %f\n' % (hits / 20.0))
    print "---------------------------------------------------"

    arq.close()
    '''