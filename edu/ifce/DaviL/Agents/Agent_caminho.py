# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:02:25 2019

@author: vitor
"""

from edu.ifce.DaviL.Agents.Agents import *
from edu.ifce.DaviL.Problems.caminho_entre_vertices_original import caminho_entre_vertices
import time


if __name__ == '__main__':
    Realizacoes = 20
    Total = 0
    list_of_agents = [AgentBreathFirstSearch(), AgentDepthFirstSearch(), AgentDepthFirstSearchExplored(), AgentIterativeDeepingSearch(),
                      AgentUnifordCostSearch(), AgentBirectionalSearch()]
    names_of_agents = ['largura', 'profundidade', 'profundidadade com visitados', 'profundidade iterativa', 'custo uniforme', 'bidirecional']

  
#    list_of_agents = [AgentDepthFirstSearchExplored(), AgentUnifordCostSearch(), AgentBirectionalSearch()]
#    names_of_agents = ['profundiade com lista de visitados', 'custo uniforme', 'bidirecional']
    arq = open('result_caminhoent.txt', 'w')
    j = 0
    for Agent in list_of_agents:
        hits = 0
        avg_time = 0
        print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print ('Agente de busca %s com 20 realizacoes' % (names_of_agents[j]))
        arq.write('+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        arq.write('Agente de busca %s com 20 realizacoes\n' % (names_of_agents[j]))
        for i in range(Realizacoes):
            print ("---------------------------------------------------")
            now = time.time()
            environment = caminho_entre_vertices()
            

            Total += 1
            uselles=(j==0)
            
            sequence = Agent(environment.initial_state, environment)
            if sequence != []:
                hits += 1


            end = time.time()
            print ('total time in %s seconds' % (end - now))

            avg_time += (end - now)
            print ("---------------------------------------------------")
        print ('average time is %s seconds' % (avg_time / 20.0))
        print ('Acurracy %f' % (hits/20.0))
        arq.write('average time is %s seconds\n' % (avg_time / 20.0))
        arq.write('Acurracy %f\n' % (hits/20.0))
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