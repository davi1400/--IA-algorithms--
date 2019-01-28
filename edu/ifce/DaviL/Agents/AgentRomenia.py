from edu.ifce.DaviL.Agents.Agents import *
from edu.ifce.DaviL.Problems.RomeniaProblem import RomeniaProblem
import time

if __name__ == '__main__':
    inicio = time.time()
    Realizacoes = 20
    Total = 0
    hits = 0
    media_time = 0
    arq = open('Resultados.txt', 'w')
    # Heuristic search
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    arq.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    arq.write('Agente de busca a estrela com 20 realizacoes\n')
    print 'Agente de busca a estrela com 20 realizacoes'
    for i in range(Realizacoes):
        print "---------------------------------------------------"
        now = time.time()
        Agent = AgentAStar()
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