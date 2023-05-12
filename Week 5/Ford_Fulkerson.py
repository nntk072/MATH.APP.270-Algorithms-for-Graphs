#! /usr/bin/env python

## This file contains a template for the Ford-Fulkerson algorithm.

from graafi3 import Graph
from BFS import *
from copy import deepcopy as copy


def FindAugPath(Gr, s, t):
    aug = []
    ## laskuri is a counter to see how many edges are processed in total
    laskuri = 0
    cond = True
    haha = []
    ## Check to see whether s and t are adjacent.
    for u in Gr.adj(s):
        laskuri += 1
        if u == t and Gr.W[(s, u)] > 0:
            aug.append(s)
            aug.append(t)
            haha.append(aug)
            cond = False
            break
    # If s and t are not adjacent, find the way to s and t
    # Moreover, find the number of edges processed
    if cond:
        haha = BFS(Gr, s, t)
        laskuri += haha[1]
    return haha[0], laskuri


## Read a set containing vertices.
def ReadNodes(filename):
    ff = open(filename, "r")
    x = ff.readlines()[0].split()
    S = []
    for i in x:
        S.append(int(i))
    return S


# Add the flows in f1 and f2.
def SumFlow(f1, f2):
    f = copy(f1)
    for u, v in f2:
        if not (u, v) in f:
            f[(u, v)] = f2[(u, v)]
        else:
            f[(u, v)] += f2[(u, v)]
    return f


## Form the residual network.
def MakeResidual(G, f):
    Gr = copy(G)
    for u, v in f:
        c = 0
        ## Copy the weight
        if (u, v) in Gr.W:
            c = Gr.W[(u, v)]
        # calculate residual capasity
        cf = c - f[(u, v)]
        if not v in Gr.AL[u]:
            Gr.addEdge(u, v)
        Gr.W[(u, v)] = cf
    return Gr


## This is only a template, and does not work. You must complete it to make it work.
def MakeAugFlow(Gr, s, t, path):
    f = {}
    if not path:
        return f
    if path[0] != s:
        raise Exception("Path not from s")
    if path[-1] != t:
        raise Exception("Path not to t")
    u = s
    ## This is the minimum capacity on the path. You must find it!
    cfp = 10000 ^ 9
    for i in range(0, len(path) - 1, 1):
        if Gr.W[(path[i], path[i + 1])] <= cfp:
            cfp = Gr.W[(path[i], path[i + 1])]
    # Tahan tarvitaan implementaatio cfp:n laskemiselle
    for v in path:
        # Skip loops and first
        if v == u:
            continue
        f[(u, v)] = cfp
        f[(v, u)] = -cfp
        if Gr.W[(u, v)] < cfp:
            raise Exception("illegal residual flow")
        u = v

    return f


def FordFulkerson(G, s, t):
    ## laskuri is a counter to see how many edges are processed in total
    laskuri = 0
    flowmagnitude = 0
    f = {}
    pp = FindAugPath(G, s, t)

    p = pp[0]
    laskuri += pp[1]
    fp = MakeAugFlow(G, s, t, p)
    f = SumFlow(f, fp)
    Gr = MakeResidual(G, f)
    i = 0
    for u, v in fp:
        flowmagnitude += fp[(u, v)]
        break
    while p and i < 1000:
        i += 1
        pp = FindAugPath(Gr, s, t)

        p = pp[0]
        laskuri += pp[1]
        fp = MakeAugFlow(Gr, s, t, p)
        f = SumFlow(f, fp)
        Gr = MakeResidual(G, f)
        for u, v in fp:
            flowmagnitude += fp[(u, v)]
            break

    print("      Laskuri laski (or Cnt): " + str(laskuri))
    print(f"      Flow magnitude (or f*) is {flowmagnitude}")
    return f


def test_function(name1, name2):
    G = Graph(name1)
    S = ReadNodes(name2)
    s = S[0]
    t = S[1]
    print(f"({name1}, {name2}):")
    FordFulkerson(G, s, t)


if __name__ == "__main__":
    test_function("testflow_10", "testset_10")
    # test_function('test_flow_simple_1','testset_simple_1')
