import networkx as nx 
import matplotlib.pyplot as plot 
import sys 
import re

n = 10000
p = 1/6

G = nx.erdos_renyi_graph(n, p)

i = nx.degree_histogram(G)

plot.ylabel('Node Degree')
plot.xlabel('Frequency')
plot.plot(i)
plot.show()