# /usr/bin/env python
from copy import deepcopy as copy


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

    def addEdge(self, u, v, w=None):
        # first we check that u is a vertex
        if not u in self.V:
            ermsg = str(u) + ' not a vertex'
            raise KeyError(ermsg)
        # if v is not a vertex:
        if not v in self.V:
            ermsg = str(v) + ' not a vertex'
            raise KeyError(ermsg)
        ### This code is for adjacency list.
        if not u in self.AL:
            self.AL[u] = []
        self.AL[u].append(v)
        ## Adjust the weight
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

    """ input method for files """

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


def BFS(g, s, e):
    """
    input BFS function for the Graph to find the shortest path from the source to sink
    the code is inherited from prog task 1..
    """
    B = {s: {'dist': 0, 'parent': [None]}}
    Q = [s]
    count = 0 # The number of processing edges
    while Q:
        u = Q.pop(0)
        d = B[u]['dist']

        try:
            for v in g.adj(u):
                # Check the weight of the edge (u, v)
                if (u, v) in g.W and g.W[(u, v)] == 0:
                    continue
                if not v in B:
                    B[v] = {'dist': d + 1, 'parent': [u]}
                    Q.append(v)
                    count += 1
                elif B[v]['dist'] == d + 1:
                    B[v]['parent'].append(u)
                    count += 1
        except:
            pass
    # Convert from the parent to the shortest path!
    paths = [[e]]
    while paths and paths[0][0] != s:

        new_paths = []
        for path in paths:
            if path[0] not in B:
                continue
            for parent in B[path[0]]['parent']:
                count += 1
                new_path = [parent] + path
                new_paths.append(new_path)
        paths = new_paths
    if paths:
        return paths[0], count
    else:
        return [], count


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
    ff = open(filename, 'r')
    x = ff.readlines()[0].split()
    S = []
    for i in x:
        S.append(int(i))
    return S


# Add the flows in f1 and f2.
def SumFlow(f1, f2):
    f = copy(f1)
    for (u, v) in f2:
        if not (u, v) in f:
            f[(u, v)] = f2[(u, v)]
        else:
            f[(u, v)] += f2[(u, v)]
    return f


## Form the residual network.
def MakeResidual(G, f):
    Gr = copy(G)
    for (u, v) in f:
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
    test_function('test_flow_simple_1', 'testset_simple_1')
    test_function('test_flow_simple_2', 'testset_simple_2')
    test_function('test_flow_simple_3', 'testset_simple_3')
    test_function('test_flow_simple_4', 'testset_simple_4')
    test_function('test_flow_simple_5', 'testset_simple_5')

    test_function('testflow_10', 'testset_10')
    test_function('testflow_100', 'testset_100')
    test_function('testflow_1000', 'testset_1000')
    test_function('testflow_10000', 'testset_10000')
