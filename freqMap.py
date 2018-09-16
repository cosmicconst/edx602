# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 23:01:56 2018

@author: schoo
"""

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if freq.get(Pattern,0) == 0: 
            freq[Pattern] = 1
        else:
            freq[Pattern] += 1
    return freq


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words