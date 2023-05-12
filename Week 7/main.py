#! /usr/bin/env python

from pelaa import *
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
