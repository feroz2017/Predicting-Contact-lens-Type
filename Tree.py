#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:27:59 2020

@author: root
"""

from math import log

def createDataset():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
def calcEntropy(dataset):
    num = len(dataset)
    labels = {}
    for vector in dataset:
        label = vector[-1]
        if label not in labels.keys():
            labels[label] = 0
        labels[label] = labels[label] + 1
    entropy = 0.0
    for key in labels:
        probability = float(labels[key])/num
        entropy = entropy - probability * log(probability,2)
    return entropy

dataset, labels = createDataset()
print(dataset)
print(calcEntropy(dataset))

    
