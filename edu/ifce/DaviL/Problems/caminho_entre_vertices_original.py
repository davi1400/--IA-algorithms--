# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:23:32 2019

@author: vitor
"""

from edu.ifce.DaviL.SearchAlgorithms import Node
from edu.ifce.DaviL.Problems import Problem
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

        self.l=2 # lado do quadrado
        self.h=10#altura
        self.c=40# comprimento do retangulo
        self.squad_limit=int((self.h*self.c)/(self.l**2))#numero máximo de quadrados
        self.squad_number=np.random.randint(15,self.squad_limit)#número de quadrados
        
        aux =np.arange(self.squad_limit)
        np.random.shuffle(aux)
        aux2=aux[:self.squad_number]
        
        
     
        self.vert=[] #vértices dos quadrados
        for i in range(self.squad_number):
            aux_y=aux2[i]%(int(self.c/self.l)) #coluna
            aux_x=aux2[i]//(int(self.c/self.l))#linha
            aux_v=np.asarray([aux_x,aux_y])
            self.vert.append(aux_v)#EB
            self.vert.append(np.add(aux_v,np.asarray([0,self.l]))) #EC           
            self.vert.append(np.add(aux_v,np.asarray([self.l,self.l])))#DC
            self.vert.append(np.add(aux_v,np.asarray([self.l,0])))#DB

        
        
        self.vert=np.asarray(self.vert)
                          

        self.matrix=np.ndarray((4*self.squad_number,),dtype=np.object)
        for i in range(0,self.squad_number):
            l1,l2,l3,l4=self.make_squad(self.vert[i*4],
                                                 self.vert[i*4+1],
                                                 self.vert[i*4+2],
                                                 self.vert[i*4+3])
            self.matrix[i*4]=l1
            self.matrix[i*4+1]=l2
            self.matrix[i*4+2]=l3
            self.matrix[i*4+3]=l4
            
        
        self.initial_state=[np.random.randint(0,self.h),0]
        
        self.goal=np.asarray([np.random.randint(0,self.h),self.c]).reshape(1,2)
        self.action=np.append(self.vert,self.goal,axis=0)
       
        
        

#    
    def make_squad(self,p1,p2,p3,p4):
        l1=[make_line([(p1[0],p1[1]),(p2[0],p2[1])])]
        l2=[make_line([(p2[0],p2[1]),(p3[0],p3[1])])]
        l3=[make_line([(p3[0],p3[1]),(p4[0],p4[1])])]
        l4=[make_line([(p1[0],p1[1]),(p4[0],p4[1])])]
        

        
        return l1,l2,l3,l4
        
    
    def intercept(self,line1):
        aux=self.matrix
        for i in range(4*self.squad_number):
            if(line1.crosses(aux[i][0])):
                return True
        return False

    def actions(self, state):
        act=self.action
        
        return self.result(state, act)

    def result(self, state, action):
        all_actions = []
#        print('vertice')
#        print(self.vert[0])
#        print('acao')
#        print(action[0])
#        print('estado')
#        print(state)

        for act in action:

            aux=make_line([(state[0],state[1]),(act[0],act[1])])
            if(not self.intercept(aux)):
                all_actions.append(act)


             

        return all_actions
    def dt1(self,p):
        p=self.initial_state
        return p

    def expand(self, parent, useless=None):
        _list = []  #
        for state in self.actions(parent.state):
            new_node = Node(state, parent, [state,parent.state], self.path_cost(parent.path_cost, parent.state, state), self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return c+np.linalg.norm(state1-state2)

    def heuristic(self, state):

        return np.linalg.norm(state-self.goal)

    def test_goal(self, state):
        if (state[0]==self.goal[0][0] and state[1]==self.goal[0][1]):
            return True
        return False
    
    def execution(self, path,action):
        for next_action in range(len(path) - 1):
            print ('Estado atual %s ir para %s' % (path[next_action], path[next_action + 1]))

        print ('Chegou em %s' % (path[len(path) - 1]))
