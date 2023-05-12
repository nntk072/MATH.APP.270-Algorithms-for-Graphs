#! /usr/bin/env python
""" Breadth-first search example """

from graafi import Graph
from BFS import *
from esim1 import *

# def ReadSet(filename):
#     ff = open(filename, 'r')
#     x = ff.readlines()[0].split()
#     S = set([])
#     for i in x:
#         S.add(int(i))
#     return S


def CountShortest(g, S, s, t):
    # Find the shortest way between two vertices
    k = BFS_shortest_paths(g, s, t)
    """
    Since k has the format: [[a,b,c,d], [a,e,f,d], [a,b,e,d],...]
          S has the format: {a,b,c,...}
    We can use "for" function to find the maximum elements in S in each paths in k, and return the largest value by
    using "if" function
    """
    value = 0
    for i in k:
        count = 0
        for u in S:
            if u in i:
                count += 1
        if count >= value:
            value = count
    return value
