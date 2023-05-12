#! /usr/bin/env python
""" Breadth-first search example """

from graafi import Graph


def BFS_shortest_paths(g, s, e):
    # Function to perform breadth-first search and return a list of shortest path
    B = {s: {"dist": 0, "parent": [None]}}
    Q = [s]
    # track the maximum length and parent of each vertex
    while Q:
        u = Q.pop(0)
        d = B[u]["dist"]
        try:
            for v in g.adj(u):
                if not v in B:
                    B[v] = {"dist": d + 1, "parent": [u]}
                    Q.append(v)
                elif B[v]["dist"] == d + 1:
                    B[v]["parent"].append(u)
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
            for parent in B[path[0]]["parent"]:
                # using traceback path, new_path will help to add the parent before the vertex
                new_path = [parent] + path
                # using new_paths to make data as type list in list, and add the traceback version continuously,
                new_paths.append(new_path)
        paths = new_paths
    return paths


""" testcode """
if __name__ == "__main__":
    g = Graph("testgraph_10")
    B = BFS(g, 1)
    print(B)
