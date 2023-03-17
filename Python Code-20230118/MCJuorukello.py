#! /usr/bin/env python
""" Monte carlo simulator for Juorukello game """
""" Number of rounds is n """

from graafi3 import Graph
from random import random 
from copy import copy


""" Pelaa(g,n) pelauttaa n kierrosta graafissa g """
def Pelaa(g, n):
    Nodes = [u for u in g.V]
    Points = {u:0 for u in g.V}
    i = 0
    while i < n:
        i += 1
        j = 0
        s = Nodes[int(random()*len(Nodes))]
        t = Nodes[int(random()*len(Nodes))]
        Messages = {s:[[]]}
        Q = [s]
        D = {s:0}
        while Q:
            u = Q.pop(0)
            d = D[u]
            if u == t:
                break
            # Pick a random message
            M = Messages[u][int(random()*len(Messages[u]))]
            for v in g.adj(u):
                if v not in D:
                    D[v] = d+1
                    Messages[v] = []
                    Q.append(v)
                # Send the random message forward
                if D[v] == d+1:
                    mm = copy(M)
                    mm.append(v)
                    Messages[v].append(mm)
        if not t in Messages:
            continue
        M = Messages[t][int(random()*len(Messages[t]))]
        for u in M:
            if u != t:
                Points[u] += 1
    return [u[0] for u in sorted(Points.items(), key = lambda x: x[1], reverse = True)]


if __name__ == "__main__":
    g = Graph('walk_random_769_8651')
    u = Pelaa(g,1000)
    print(u)
