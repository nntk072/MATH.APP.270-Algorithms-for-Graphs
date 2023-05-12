"""
Name: Long Nguyen

Since using import will need the marker to have the file inside the directory, I had copied all the necessary important
functions and class into this file for easy testing
Moreover, in main function, I will list all the test cases in Moodle.

To run this file, you just need to extract the zip file and run (in Pycharm).


Task: Find the shortest length from the beginning and ending vertices to move using BFS algorithm and something related.
"""
from CountShortest_dum import *

def Testfunction(g, B, a, b):
    # Combining the aspects and return the largest amount of elements in digraph in the shortest path from vertex a to B
    g = Graph(g)
    B = ReadSet(B)
    # Checking if the beginning and ending vertices are in the graph.
    if a not in g.V or b not in g.V:
        return f"can't find the road since there aren't at least one or two vertices in the graph"
    x = CountShortest(g, B, a, b)
    return x


def main():
    """
    Since I have zipped all the necessary files, you just need to run the file and see the results
    """

    # Checking from the "Example graphs and some Python code"
    print(
        f"Test the code with the one simple example provided (testgraph_harkka, testset1)."
    )
    print(f"Harkka, Set 1:       {Testfunction('testgraph_harkka', 'testset1', 1, 6)}")

    # Checking all Simple tests
    print(f"\nTest the code with the simple test provided in folder Simple_tests")
    print(
        f"Sensible 0, Set 0:   {Testfunction('testgraph_sensible0', 'testset_sensible0', 1, 1)}"
    )
    print(
        f"Sensible 0, Set 0_b: {Testfunction('testgraph_sensible0', 'testset_sensible0_b', 1, 1)}"
    )
    print(
        f"Sensible 1, Set 1_a: {Testfunction('testgraph_sensible1', 'testset_sensible1_a', 1, 10)}"
    )
    print(
        f"Sensible 1, Set 1_b: {Testfunction('testgraph_sensible1', 'testset_sensible1_b', 1, 10)}"
    )
    print(
        f"Sensible 2, Set 2_a: {Testfunction('testgraph_sensible2', 'testset_sensible2_a', 1, 10)}"
    )
    print(
        f"Sensible 2, Set 2_b: {Testfunction('testgraph_sensible2', 'testset_sensible2_b', 1, 10)}"
    )

    # Checking 10 tests
    print(f"\nTest the code with 10 tests provided in folder Ten tests")
    print(f"Graph 1, Set 1:      {Testfunction('testgraph_1', 'testset_1', 1, 10)}")
    print(f"Graph 2, Set 2:      {Testfunction('testgraph_2', 'testset_2', 1, 20)}")
    print(f"Graph 3, Set 3:      {Testfunction('testgraph_3', 'testset_3', 1, 30)}")
    print(f"Graph 4, Set 4:      {Testfunction('testgraph_4', 'testset_4', 1, 40)}")
    print(f"Graph 5, Set 5:      {Testfunction('testgraph_5', 'testset_5', 1, 50)}")
    print(f"Graph 6, Set 6:      {Testfunction('testgraph_6', 'testset_6', 1, 60)}")
    print(f"Graph 7, Set 7:      {Testfunction('testgraph_7', 'testset_7', 1, 70)}")
    print(f"Graph 8, Set 8:      {Testfunction('testgraph_8', 'testset_8', 1, 80)}")
    print(f"Graph 9, Set 9:      {Testfunction('testgraph_9', 'testset_9', 1, 90)}")
    print(f"Graph 10, Set 10:    {Testfunction('testgraph_10', 'testset_10', 1, 100)}")


if __name__ == "__main__":
    main()
