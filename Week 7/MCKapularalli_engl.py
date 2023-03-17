#! /usr/bin/env python
""" Monte carlo simulator for Kapularalli (Pass-the-baton) game """
""" the "Jump probability" can be varied """

from graafi3 import Graph
from random import random 
import numpy as np

""" Play the game for n rounds using an unweighted digraph g"""
def Pelaa_uw(g, n, d):
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        u = Nodes[int(random()*len(Nodes))]
        k = 2*len(Nodes)
        while j < k:
            j += 1
            if random() <= d or len(g.adj(u)) == 0:
                u = Nodes[int(random()*len(Nodes))]
                continue
            A = g.adj(u)
            u = A[int(random()*len(A))]
        Points[u] += 1
    return [u[0] for u in sorted(Points.items(), key = lambda x: x[1], reverse = True)]

""" Play the game for n rounds using a weighted digraph g"""
def Pelaa_weight(g, n, d):
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        u = Nodes[int(random()*len(Nodes))]
        k = 2*len(Nodes)
        while j < k:
            j += 1
            if random() <= d or len(g.adj(u)) == 0:
                u = Nodes[int(random()*len(Nodes))]
                continue
            wght = np.cumsum([g.W[(u,v)] for v in g.adj(u)])
            u_i = np.argmax(wght > random()*wght[-1])
            u = g.adj(u)[u_i]
        Points[u] += 1
    return [u[0] for u in sorted(Points.items(), key = lambda x: x[1], reverse = True)]

if __name__ == "__main__":
    g = Graph('preferential_random_101_177')
    u = Pelaa_weight(g,10000, 0.4)
    print(u[:10])
