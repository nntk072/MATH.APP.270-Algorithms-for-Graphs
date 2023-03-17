import networkx as nx
import matplotlib.pyplot as plt

filename = 'testgraph.txt'
file = open(filename)

G = nx.DiGraph()

#reads the file
for row in file:

    starting_vertice = row[0]

    #forms the graph, from the file
    for value in row:
        if value != starting_vertice and value != ":" and value != " " and value != "\n": #removes aything else than the numbers

            G.add_edges_from([(starting_vertice, value)])   #adding to graph

nx.draw_networkx(G,cmap = plt.get_cmap('jet'), arrows=True) #draws the graph

plt.show()
file.close()

