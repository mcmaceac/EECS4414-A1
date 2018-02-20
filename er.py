import networkx as nx 
import matplotlib.pyplot as plot 
import sys 
import re

n = 1000
p = 1/6
G = nx.erdos_renyi_graph(n, p)

i = nx.degree_histogram(G)
plot.ylabel('Node Degree')
plot.xlabel('Frequency')
plot.plot(i)
plot.show()

clust = nx.clustering(G)
x = list(clust.keys())
y = list(clust.values())
plot.ylabel('Clustering Coefficient')
plot.xlabel('Node Number')
plot.plot(x, y)
plot.show()