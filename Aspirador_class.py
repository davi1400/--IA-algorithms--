# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:42:21 2019

@author: vitor
"""

from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from edu.ifce.DaviL.SearchAlgorithms.Problem import Problem
from random import shuffle
import numpy as np
import copy


class Aspirador(Problem):

    def __init__(self):
        #clean: 1 = dirt 0 = clean
        #go: 1 = can't 0 = can
        #turn left l = can't 0 = can
        #turn right l = can't 0 = can
        #(i,j) = indices
        #head: 0=N
        self.l=3#linha
        self.c=3#coluna
        self.initial_state = np.append(np.array([1,1,0,0]),np.append(np.random.randint(0,3,2),np.random.randint(0,4,1)))
        self.world=np.random.randint(0,2,(self.l,self.c))#mundo
        self.ind=self.initial_state[4:6]#indices
        self.initial_state[0]=self.world[self.ind[0]][self.ind[1]]
#        if(self.ind[0]==0):#primeira linha
#            if(self.initial_state[6]==1):#não é possivel dobrar a esquerda
#                self.initial_state[2]=1
#            elif(self.initial_state[6]==3):#não é possivel dobrar a direita
#                self.initial_state[3]=1
#        elif(self.ind[0]==(self.l-1)):#ultima linha
#            if(self.initial_state[6]==1):#não é possivel dobrar a esquerda
#                self.initial_state[2]=1
#            elif(self.initial_state[6]==3):#não é possivel dobrar a direita
#                self.initial_state[3]=1
#        elif(self.ind[1]==0):#primeira coluna
#            if(self.initial_state[6]==2):#não é possivel dobrar a esquerda
#                self.initial_state[2]=1
#            elif(self.initial_state[6]==0):#não é possivel dobrar a direita
#                self.initial_state[3]=1        
#        elif(self.ind[1]==(self.c-1)):#ultima coluna
#            if(self.initial_state[6]==2):#não é possivel dobrar a esquerda
#                self.initial_state[2]=1
#            elif(self.initial_state[6]==0):#não é possivel dobrar a direita
#                self.initial_state[3]=1 
        self.initial_state=[self.initial_state,self.world]
        self.initial_state=self.change(self.initial_state)
        

    def actions(self, state):
        actions = ['GO', 'SUD', 'TURNL','TURNR']

        if state[0][0] == 0:#está limpo
            actions.remove('SUD')

        if state[0][1]==1:#não pode prosseguir
            actions.remove('GO')
            
        if state[0][2] == 0:#virar a esquerda não poderá prosseguir
            actions.remove('TURNL')

        if state[0][3]==1:#virar a direita não poderá proseguir
            actions.remove('TURNR')        


        print(actions)
        return self.result(state, actions)

    def result(self, state, actions):
        all_actions = []

        for act in actions:
            print(act)
            aux=copy.deepcopy(state)

            if(act is 'SUD'):#limpar
                aux[1][aux[0][4]][aux[0][5]]=0
                aux[0][0]=0
                all_actions.append([aux, act])
            elif(act is 'GO'):#ir
                if(aux[0][6]==0):#Norte
                    aux[0][4]=aux[0][4]-1
                     
                        
                elif(aux[0][6]==1):#Leste
                    aux[0][5]=aux[0][5]+1
                   
                elif(aux[0][6]==2):#Sul
                    aux[0][4]=aux[0][4]+1

                else:#Oeste
                    aux[0][5]=aux[0][5]-1
 
                
            elif(act is 'TURNR'):#Virar a direita
                aux[0][6]=(aux[0][6]+1)%4

                
            else:#Virar a esquerda
                aux[0][6]=(aux[0][6]-1)%4

            aux = self.change(aux) 
            print(aux)
            all_actions.append([aux, act])
                        
             

        return all_actions
    def dt1(self,p):
        p=self.initial_state
        return p

    def expand(self, parent):
        _list = []  #
        for state, act in self.actions(parent.state):
            new_node = Node(state, parent, act, self.path_cost(parent.path_cost, parent.state, state), self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return c + 1

    def heuristic(self, state):

        return (100*(len(np.where(state[1]==0)[0])))

    def test_goal(self, state):
        if (np.sum(state[1])==0):
            return True
        return False

    def execution(self, path):
        for next_action in range(len(path) - 1):
            print (path[next_action])
        print (path[len(path) - 1])
        return

    
    def change(self,aux):
        #não poderá prosseguir na próxima interação
        if((aux[0][6]==0 and aux[0][4]==0)
                   or (aux[0][6]==1 and (aux[0][5]==(self.c-1)))
                   or (aux[0][6]==2 and(aux[0][4]==(self.l-1)))
                   or (aux[0][6]==3 and aux[0][5]==0)):
            aux[0][1]=1
                #não poderá dobrar a esquerda ná próxima interação
        if((aux[0][6]==0 and aux[0][5]==0)
                   or (aux[0][6]==1 and (aux[0][4]==(0)))
                   or (aux[0][6]==2 and(aux[0][4]==(self.c-1)))
                   or (aux[0][6]==3 and aux[0][5]==(self.l-1))):
            aux[0][2]=1   
                #não poderá dobrar a direita ná próxima interação
        if((aux[0][6]==0 and aux[0][5]==(self.c-1))
                   or (aux[0][6]==1 and (aux[0][4]==(self.l-1)))
                   or (aux[0][6]==2 and(aux[0][5]==(0)))
                   or (aux[0][6]==3 and aux[0][4]==(0))):
            aux[0][3]=1    
        return aux