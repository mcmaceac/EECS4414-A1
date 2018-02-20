import networkx as nx 
import matplotlib.pyplot as plot 
import sys 
import re

n = 10000
p = 1/6

G = nx.erdos_renyi_graph(n, p)

nx.draw(G)
plot.show(G)