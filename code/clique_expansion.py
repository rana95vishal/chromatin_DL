#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:04:46 2024

@author: vishalr
"""



edge_list = []

with open('hyperedge_list.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        l = line[:-1].split('\t')
        
        for e1 in l:
            for e2 in l:
                if(e1 != e2):
                    edge_list.append(e1+'\t'+e2)
                    
edge_list = list(set(edge_list))
                    
with open('edge_list.py', 'w') as f:
    for l in edge_list:
        f.write(l)
        f.write('\n')

'''

#generate a random hypergraph to test

import random

with open('hyperedge_list.txt', 'w') as f:
    for itr in range(500):
        l = random.sample(range(1, 2000), random.randint(1,4))
        for num in l:
            f.write(str(num))
            f.write('\t')
        f.write('\n')
'''