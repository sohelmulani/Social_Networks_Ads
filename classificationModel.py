#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 10:26:14 2019

@author: sohel
"""

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


class LogisticClassifier(object):
    
    def __init__(self):
        pass
    
    def fit(self,x,y):
        classifier=LogisticRegression(random_state=0)
        c=classifier.fit(x,y)
        return(c)
        
class DecisionTreeClassifier(object):
    
    def __init__(self):
        pass

    def fit(self,x,y):
        classifier=DecisionTreeClassifier(self, class_weight=None, criterion='gini', max_depth=None,
			max_features=None, max_leaf_nodes=None, random_state=0,
			splitter='best')
        c=classifier.fit(x,y)
        return(c)
        
    def __del__(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        