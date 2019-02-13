
from edu.ifce.DaviL.SearchAlgorithms.Node import Node
from Problem import Problem
from random import shuffle
import numpy as np
import copy


class Aspirador(Problem):

    def __init__(self):
        # clean: 1 = dirt 0 = clean
        # go: 1 = can't 0 = can
        # turn left l = can't 0 = can
        # turn right l = can't 0 = can
        # (i,j) = indices
        # head: 0=N
        self.l = 3  # linha
        self.c = 3  # coluna
        self.initial_state = [np.random.randint(0, (self.l - 1)), np.random.randint(0, (self.c - 1))]
        self.world = np.random.randint(0, 2, (self.l, self.c))  # mundo
        self.initial_state = [self.initial_state, self.world]

    def actions(self, state):
        actions = ['SUD', 'UP', 'DOWN', 'LEFT', 'RIGHT']

        if state[1][state[0][0]][state[0][1]] == 0:  # esta limpo
            actions.remove('SUD')

        if state[0][0] >= (self.c - 1):  # nao pode prosseguir para direita
            actions.remove('LEFT')

        if state[0][0] <= 0:  # nao pode prosseguir para esquerda
            actions.remove('RIGHT')

        if state[0][1] >= (self.l - 1):  # nao pode prosseguir para cima
            actions.remove('UP')

        if state[0][1] <= 0:  # nao pode processeguir para baixo
            actions.remove('DOWN')

        return self.result(state, actions)

    def result(self, state, actions):
        all_actions = []

        for act in actions:
            aux = copy.deepcopy(state)

            if (act is 'SUD'):  # limpar
                aux[1][aux[0][0]][aux[0][1]] = 0

            elif (act is 'LEFT'):  # ir
                aux[0][0] += 1

            elif (act is 'RIGHT'):  # ir
                aux[0][0] -= 1


            elif (act is 'UP'):  # Virar a direita
                aux[0][1] += 1


            else:  # Virar a esquerda
                aux[0][1] -= 1

            all_actions.append([aux, act])

        return all_actions

    def dt1(self, p):
        p = self.initial_state
        return p

    def expand(self, parent, useless=None):
        _list = []  #
        for state, act in self.actions(parent.state):
            new_node = Node(state, parent, act, self.path_cost(parent.path_cost, parent.state, state),
                            self.heuristic(state))
            _list.append(new_node)
        shuffle(_list)
        return _list

    def path_cost(self, c, state1, state2):
        return c + 1

    def heuristic(self, state):
        cont = np.asarray(np.where(state[1] == 1))
        aux = 10 * len(cont[0])
        for i in range(len(cont[0])):
            aux += np.linalg.norm(state[0] - cont.T[i])

        return aux

    def test_goal(self, state):
        if (np.sum(state[1]) == 0):
            return True
        return False

    def execution(self, path, action):

        for next_action in range(len(path) - 1):
            print(np.reshape(path[next_action][1], (3, 3)))
            print(action)

        print(np.reshape(path[len(path) - 1][1], (3, 3)))
        return path
