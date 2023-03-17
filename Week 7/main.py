#! /usr/bin/env python

from random import random
from graafi3 import Graph

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


def comparing_output(g, n):
    """
    Compare the output of the Monte Carlo simulation and the output of the PageRank Algorithm.
    Args:
        g (str): The name of the file
        n (int): The number of rounds
    """
    # Check invalid number of rounds
    if n <= 0:
        print("Invalid number of rounds, please change the number of rounds > 0")
        return
    try:
        graph = Graph(g)
        players = Pelaa(graph, n)
        print(f"File: {g}, Number of rounds: {n}")
        print(f"Output from Monte Carlo simulation:\n{players[0]}")
        print(f"Output from Algorithm in loop:\n{players[1]}")
        for i in range(0, len(players[0])):
            if players[0][i] != players[1][i]:
                print(f"\n     The list of nodes from Monte Carlo and PageRank algo for the loop is not the same\n")
                return
        print(f"\n     The list of nodes from Monte Carlo and PageRank algo for the loop is the same\n")
        print(f"Output from PageRank algorithm:\n{players[2]}")
    except FileNotFoundError:
        print("File not found,please try again for the input or add some file")
        return


def main():
    """comparing_output('preferential_random_10_14', 100)
    comparing_output('preferential_random_10_31', 100)"""
    comparing_output('preferential_random_101_177', 100)
    """comparing_output('preferential_random_101_1053', 100)
    comparing_output('preferential_random_354_7768', 100)
    comparing_output('simply_random_101_1053', 100)
    comparing_output('simply_random_354_1231', 100)
    comparing_output('simply_random_weighted_102_817', 100)
    comparing_output('walk_random_101_512', 1000)
    comparing_output('walk_random_354_1231', 1000)
    comparing_output('walk_random_769_27156',1000)"""
if __name__ == "__main__":
    main()
