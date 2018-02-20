import networkx as nx 
import matplotlib.pyplot as plt 
import sys 
import re
import collections

def extract_lengths(dict):
	result = []
	for dictionary in dict:
		for length in dictionary.values():
			result.append(length)
	return result

n = 5
p = 1/6
G = nx.erdos_renyi_graph(n, p)

shortestPathDicts = list(nx.shortest_path_length(G).values())
print(shortestPathDicts)
print(extract_lengths(shortestPathDicts))

#print(collections.Counter(nx.shortest_path_length(G)))

nx.draw(G, node_size = [3 for v in G], with_labels = True)
plt.show()
