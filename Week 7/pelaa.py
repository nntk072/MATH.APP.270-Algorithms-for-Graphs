#! /usr/bin/env python
""" Monte carlo simulator for Kapularalli (Pass-the-baton) game """
""" the "Jump probability" can be varied """

from graafi3 import Graph
from random import random 
import numpy as np

def pagerank(g, d):
    """
    Calculate the PageRank of each node in the graph g.
    Args:
        g (Class Object): Graph object
        d (float): input parameter d

    Returns:
        dict: dictionary of nodes and their PageRank values
    """
    
    Nodes = [u for u in g.V]
    n = len(Nodes)
    prob = {u: 1/n for u in Nodes}
    d_sum = (1-d)/n  # sum of PageRank values for dangling nodes
    for i in range(0, 10000):
        new_prob = {u: d_sum for u in Nodes}  # initialize PageRank values for dangling nodes
        for u in Nodes:
            if len(g.adj(u)) == 0:
                continue
            for v in g.adj(u):
                new_prob[v] += d*prob[u]/len(g.adj(u))
        prob = new_prob  # update PageRank values
        prob = {u: prob[u] + d_sum for u in Nodes}  # add sum of PageRank values for dangling nodes
        # check for convergence
        err = sum(abs(prob[u] - new_prob[u]) for u in Nodes)
        if err < 1e-6:
            break
    return prob

def Pelaa(g, n):
    """
    Play n rounds in the graph g.
    Args:
        g (Class Object): Graph object
        n (int): input parameter d

    Returns:
        list: list of players with Monte Carlo simulation
        list: list of players with PageRank Algorithm
    """
    d = 0.1
    Nodes = [u for u in g.V]
    Points_from_Monte = Points_from_PageRank = {u: 0 for u in g.V}
    prob = pagerank(g, d)
    i = 0
    while i < n:
        i += 1
        j = 0
        u = Nodes[int(random()*len(Nodes))]
        k = 2*len(Nodes)
        while j < k:
            j += 1
            A = g.adj(u)
            if len(A) == 0:
                if random() <= 1-d:
                    u = Nodes[int(random()*len(Nodes))]
                continue
            if random() <= d:
                u = Nodes[int(random()*len(Nodes))]
                continue
            

            # Random value for adding in Monte
            u_monte = A[int(random()*len(A))]
            
            # Random value for adding in PageRank
            probabilities = [prob[v] for v in A]
            u_pagerank = A[probabilities.index(max(probabilities))]
            

        Points_from_Monte[u_monte] += 1
        Points_from_PageRank[u_pagerank] += 1
    return [u[0] for u in sorted(Points_from_PageRank.items(), key=lambda x: x[1], reverse=True)], [u[0] for u in sorted(Points_from_Monte.items(), key=lambda x: x[1], reverse=True)], [u[0] for u in sorted(prob.items(), key=lambda x: x[1], reverse=True)]

