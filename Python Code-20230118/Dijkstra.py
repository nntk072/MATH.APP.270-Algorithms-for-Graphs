#! /usr/bin/env python
""" Dijkstra-search example """

from graafi3 import Graph
from PQ import PQ





""" dijkstra search from s. Returns a dictionary of nodes with 
    D[u] = d, such that d is the distance from s """

## This is the relaxation function. Returns "true" if and only if the 
## distance is smaller from u to v. 
def relax(u,v,g,D):
    dd = g.W[(u,v)]
    if not v in D:
        D[v] = D[u] + dd
        return True
    if D[v] > D[u] + dd:
        D[v] = D[u] + dd
        return True
    return False



def Dijkstra(g, s):
    Q = PQ()
    D = {}
    D[s] = 0
    Q.push((0,s))
    #print(Q.H + ", " len(Q.H))
    while not Q.empty():
        (d, u) = Q.pop()
        #print(u)
        for v in g.adj(u):
            #print ("-->" + str(v))
            if not Q.done(v):
                if relax(u,v,g,D):
                    Q.push((D[v], v))
    return D



""" testcode """
if __name__ == "__main__":
    g = Graph('../testgraph_weighted')
    D = Dijkstra(g,1)
    print(D)

