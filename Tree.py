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
def chooseBestFeature(dataset):
    num = len(dataset[0]) - 1
    baseEntropy= calcEntropy(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(num):
        featList = [example[i] for example in dataset]
        uniqueVal = set(featList)
        newEntropy = 0.0
        '''splitting data on each feature and then calculating entropy 
        for that feature then it is subtracted by baseEntropy (information Gain)
        '''
        for value in uniqueVal:
            subDataset = splitdataset(dataset,i,value)
            prob = len(subDataset)/float(len(dataset))
            newEntropy = prob * calcEntropy(subDataset)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

dataset, labels = createDataset()
#print(dataset)
#print(calcEntropy(dataset))
#redData = splitdataset(dataset,1,1)
#print(redData)
#print(dataset)
print(chooseBestFeature(dataset))

    
