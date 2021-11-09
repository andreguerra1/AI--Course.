#Grupo 105 André Guerra 86382 Tomás Zaki 79690
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

from itertools import product

gra = [[],[],[0,1],[2],[2]]
ev = (1,1,1,1,1)




class Node():
    
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
    
    def computeProb(self, evid):
        
        if len(self.prob) == 1:
            probT = self.prob[0]
            return [1-probT,probT]
        
        
        aux = self.prob
        

        for e in self.parents:
            index = evid[e]
            aux = aux[index]
            
        probT = aux
        probF = 1-probT
        res = [probF,probT]
                
        return res
    
    
    
class BN():
    
    def __init__(self, gra, prob):
        self.graph = gra
        self.prob = prob

    def computePostProb(self, evid):
        
        sumT = 0
        sumF = 0
        
        lst = getEvidCombinations(evid)
        combinations = lst[0]
        objectiveIndex = lst[1]
        indices = lst[2]
        
        for e in combinations:
            newEvid = list(evid)
            newEvid[objectiveIndex] = 1
            for i in range(len(indices)):
                newEvid[indices[i]] = e[i]
            sumT += self.computeJointProb(tuple(newEvid))
                
        for e in combinations:
            newEvid = list(evid)
            newEvid[objectiveIndex] = 0
            for i in range(len(indices)):
                newEvid[indices[i]] = e[i]
            sumF += self.computeJointProb(tuple(newEvid)) 
        
        return sumT/(sumT+sumF)
        
        
                      
        
    def computeJointProb(self, evid):
        res = 1
        
        for i in range(len(evid)):
            node = self.prob[i]
            index = evid[i]
            res *= node.computeProb(evid)[index]            
        
        return res


def getEvidCombinations(evid):
    indices = []
    cnt = 0
    lst = []
    i = 0
    
    for e in evid:
        if e == [] :
            cnt +=1
            indices += [i]
        elif e == -1:
            objectiveIndex = i           
        i+=1
    aux = [list(product([0,1],repeat = cnt)), objectiveIndex,indices]
    
    return aux
    


    

