"""
Name: Long Nguyen

Since using import will need the marker to have the file inside the directory, I had copied all the necessary important
functions and class into this file for easy testing
Moreover, in main function, I will list all the test cases in Moodle.

To run this file, you just need to extract the zip file and run (in Pycharm).


Task: Find the shortest length from the beginning and ending vertices to move using BFS algorithm and something related.
"""


class Graph:
    """ class initializer """

    def __init__(self, filename=None):
        # initialize to empty graph
        # Placeholder for keys to vertices
        self.V = set([])
        # number of vertices
        self.nV = 0
        # number of edges
        self.nE = 0
        # Placeholder for adjacency matrix
        self.AM = {}
        # Placeholder for adjacency list.
        self.AL = {}
        # placeholder for weight
        self.W = {}
        if filename:
            self.readfile(filename)

    def addVertex(self, k):
        if k in self.V:
            return
        # Add an element to the vertex set
        self.AL[k] = []
        self.V.add(k)
        self.nV += 1

    def addEdge(self, u, v, w=None):
        # first we check that u is a vertex
        if not u in self.V:
            ermsg = str(u) + ' not a vertex'
            raise KeyError(ermsg)
        # if v is not a vertex:
        if not v in self.V:
            ermsg = str(v) + ' not a vertex'
            raise KeyError(ermsg)
        # This code is for adjacency list.
        if not u in self.AL:
            self.AL[u] = []
        self.AL[u].append(v)
        self.nE += 1
        # Adjust the weight
        if not w is None:
            self.W[(u, v)] = w

    def adj(self, u):
        # return an iterable of elements adjacent to u
        if u in self.AL:
            return self.AL[u]
        else:
            return []

    def isAdj(self, u, v):
        # Return true if (u,v) is an edge
        for i in self.AL[u]:
            if v == i:
                for t in self.AL[v]:
                    if u == t:
                        return True
        return False

    def readfile(self, filename):
        ff = open(filename, 'r')
        for ll in ff.readlines():
            try:
                u = int(ll.split(':')[0].strip())
            except:
                continue
            if not u in self.V:
                self.addVertex(u)
            for vv in ll.split(':')[1].split():
                try:
                    v = int(vv)
                except:
                    uv = vv.strip('()').split(',')
                    v = int(uv[0])
                    w = float(uv[1])
                    self.addVertex(v)
                    self.addEdge(u, v, w)
                    continue
                if not v in self.V:
                    self.addVertex(v)
                self.addEdge(u, v)

    def writefile(self, filename):
        ff = open(filename, 'w')
        i = 0
        weighted = False
        if self.W:
            weighted = True
        for u in self.V:
            i += 1
            ff.write(str(u))
            ff.write(": ")
            for v in self.AL[u]:
                if not weighted:
                    ff.write(str(v))
                else:
                    ff.write("(" + str(v) + "," + str(self.W[(u, v)]) + ")")
                ff.write(" ")
            if i < len(self.V):
                ff.write('\n')


def ReadSet(filename):
    # Read file and return digraph as type [a,b,c,...]
    ff = open(filename, 'r')
    x = ff.readlines()[0].split()
    S = set([])
    for i in x:
        S.add(int(i))
    return S


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


def BFS_shortest_paths(g, s, e):
    # Function to perform breadth-first search and return a list of shortest path
    B = {s: {'dist': 0, 'parent': [None]}}
    Q = [s]
    # track the maximum length and parent of each vertex
    while Q:
        u = Q.pop(0)
        d = B[u]['dist']
        try:
            for v in g.adj(u):
                if not v in B:
                    B[v] = {'dist': d + 1, 'parent': [u]}
                    Q.append(v)
                elif B[v]['dist'] == d + 1:
                    B[v]['parent'].append(u)
        except:
            pass
    # After the function, we can get the largest distance and the longest the parent of each vertex from the
    # beginning. print(B) for understanding
    paths = [[e]]
    # make a list of all shortest paths, stop when finding the beginning
    while paths[0][0] != s:
        new_paths = []
        # traceback by parents from the ending to the beginning to find the shortest path
        for path in paths:
            for parent in B[path[0]]['parent']:
                # using traceback path, new_path will help to add the parent before the vertex
                new_path = [parent] + path
                # using new_paths to make data as type list in list, and add the traceback version continuously,
                new_paths.append(new_path)
        paths = new_paths
    return paths


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
    print(f"Test the code with the one simple example provided (testgraph_harkka, testset1).")
    print(f"Harkka, Set 1:       {Testfunction('testgraph_harkka', 'testset1', 1, 6)}")

    # Checking all Simple tests
    print(f"\nTest the code with the simple test provided in folder Simple_tests")
    print(f"Sensible 0, Set 0:   {Testfunction('testgraph_sensible0', 'testset_sensible0', 1, 1)}")
    print(f"Sensible 0, Set 0_b: {Testfunction('testgraph_sensible0', 'testset_sensible0_b', 1, 1)}")
    print(f"Sensible 1, Set 1_a: {Testfunction('testgraph_sensible1', 'testset_sensible1_a', 1, 10)}")
    print(f"Sensible 1, Set 1_b: {Testfunction('testgraph_sensible1', 'testset_sensible1_b', 1, 10)}")
    print(f"Sensible 2, Set 2_a: {Testfunction('testgraph_sensible2', 'testset_sensible2_a', 1, 10)}")
    print(f"Sensible 2, Set 2_b: {Testfunction('testgraph_sensible2', 'testset_sensible2_b', 1, 10)}")

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
