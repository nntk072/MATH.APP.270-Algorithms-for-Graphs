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
