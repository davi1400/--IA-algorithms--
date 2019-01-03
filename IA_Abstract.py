# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:43:25 2019

@author: vitor
"""

from abc import ABC, abstractmethod

class No(ABC):
    def __init__(self, valor,pai):
        self.valor = valor
        self.pai=pai
          
    @abstractmethod
#Chama todos os pais até pai == null, se culto==True ele retorna o custo do camino
#se for falso retorna a penas o caminho    
    def caminho(self,custo):
        pass

class Problema(ABC):
    def __init__(self, estado_inicial,objetivo):
        self.estado_inicial = estado_inicial#Cada estado é um nó
        self.objetivo=objetivo    
    @abstractmethod
    def funcao_sucessora(self,estado_atual):#retorna estados alcançáveis
        pass

class Agente(ABC):
    @abstractmethod
    def __init__(self,problema,borda):
        self.problema = problema
        self.borda=borda    
    def teste_objetivo(self,no_atual):
        pass
    def retirar_borda(self):
        pass
    def adiciona_borda(self):
        pass
    def busca(self):
        pass