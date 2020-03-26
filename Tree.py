#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:27:59 2020

@author: root
"""

from math import log

def createDataset():
    dataSet = [[1, 1,2, 'yes'],
               [1, 1,3, 'yes'],
               [1, 0,2, 'no'],
               [0, 1,3, 'no'],
               [0, 1,2, 'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
''' Calculating the Entropy'''
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

'''Spliting dataset on base of feature'''
def splitdataset(dataset,axis,value):
    retDataset = []
    for vector in dataset:
        if vector[axis] == value:
            reducedV = vector[:axis]
            reducedV.extend(vector[axis+1:])
            retDataset.append(reducedV)
    return retDataset
dataset, labels = createDataset()
print(dataset)
#print(calcEntropy(dataset))
redData = splitdataset(dataset,1,1)
print(redData)

    
