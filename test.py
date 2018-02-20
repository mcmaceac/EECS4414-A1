import networkx as nx 
import matplotlib.pyplot as plt 
import sys 
import re

n = 100
p = 1/6
G = nx.erdos_renyi_graph(n, p)

#print(nx.all_pairs_shortest_path_length(G))

nx.draw(G)
plt.show