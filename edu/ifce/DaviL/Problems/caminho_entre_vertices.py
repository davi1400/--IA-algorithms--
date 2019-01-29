# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:23:32 2019

@author: vitor
"""
from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from edu.ifce.DaviL.SearchAlgorithms.Problem import Problem
from random import shuffle
import numpy as np
from shapely.geometry import LineString as make_line
import pip

try:
    __import__('shapely')
except ImportError:
    acept=input('You dont have the Shapely package. Would you like install it?')
    if(acept=='Yes'):
        pip.main(['install', 'shapely']) 
    
class caminho_entre_vertices(Problem):

    def __init__(self):

        self.l=2 # largura do quadrado
        self.h=10#altura
        self.c=40#coluna
        self.squad_limit=int((self.h*self.c)/(self.l**2))#numero máximo de quadrados
        self.squad_number=np.random.randint(15,self.squad_limit)#número de quadrados
        
        aux=np.asarray(np.random.shuffle(np.arange(1,(self.c-self.l),self.l))[:self.squad_number],
             np.random.shuffle(np.arange(1,(self.c-self.l),self.l))[:self.squad_number]).T
        
        self.vert=[] #vértices dos quadrados
        for i in range(self.squad_number):
            self.vert.append(aux[i])#EB
            self.vert.append(np.add(aux[i],np.asarray([0,self.l]))) #EC           
            self.vert.append(np.add(aux[i],np.asarray([self.l,self.l])))#DC
            self.vert.append(np.add(aux[i],np.asarray([self.l,0])))#DB
        self.vert.reshape(self.squad_number,4)
                          
        self.matrix=self.make_squad(self.vert[i],
                                   self.vert[i+1],
                                   self.vert[i+2],
                                   self.vert[i+3])#arestas
        
        for i in range(4,self.squad_number,4):
            self.matrix=np.append(self.matrix,
                                  self.make_squad(self.vert[i],
                                                 self.vert[i+1],
                                                 self.vert[i+2],
                                                 self.vert[i+3]),axis=0)
        self.initial_state=[0,np.random.randint(0,self.h)]
        
        self.goal=[self.c,np.random.randint(0,self.h)]
        
        self.action=np.append(self.vert,self.get_goal,axis=0)
            
        
        
            
#    def make_line(p1,p2):
#        if(p1[0]<p2[0]):
#            x1=p1
#            x2=p2
#        else:
#            x1=p2
#            x2=p1
#        a=(x2[1]-x1[1])/(x2[0]-x1[0])
#        b=x2[1]-a*x2[0]
#        return a,b
#    
    def make_squad(self,p1,p2,p3,p4):
        l1=[make_line([(p1[0],p1[1]),(p2[0],p2[1])])]
        l2=[make_line([(p2[0],p2[1]),(p3[0],p3[1])])]
        l3=[make_line([(p3[0],p3[1]),(p4[0],p4[1])])]
        l4=[make_line([(p1[0],p1[1]),(p4[0],p4[1])])]
        
        m=[[l1],
            [l2],
            [l3],
            [l4]]
        
        return m
        
    
    def intercept(self,line1):
        aux=np.reshape(self.matrix,(4*self.squad_number))
        for i in range(4*self.squad_number):
            if(line1.crosses(aux[i])):
                return True
        return False

    def actions(self, state):
        actions=self.actions
        
        return self.result(state, actions)

    def result(self, state, actions):
        all_actions = []

        for act in actions:
            aux=make_line([(state[0],state[1]),(act[0],act[1])])
            if(not self.intercept(aux)):
                all_actions.append(act)


             

        return all_actions
    def dt1(self,p):
        p=self.initial_state
        return p

    def expand(self, parent, useless):
        _list = []  #
        for state in self.actions(parent.state):
            new_node = Node(state, parent, [state,parent.state], self.path_cost(parent.path_cost, parent.state, state), self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return np.linalg.norm(state1-state2)

    def heuristic(self, state):

        return np.linalg.norm(state-self.goal)

    def test_goal(self, state):
        if (state[0]==self.goal[0] and state[1]==self.goal[1]):
            return True
        return False
    
    def execution(self, path,action):
        for next_action in range(len(path) - 1):
            print ('Estado atual %s ir para %s' % (path[next_action], path[next_action + 1]))

        print ('Chegou em %s' % (path[len(path) - 1]))
