import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np
import sys 
import re
import collections

def extract_length_distribution(dict):
	#this function takes the list of dictionaries from the shortest_path_length function
	#and extracts the path lengths to return a dictionary of the number of shortest path lengths
	#where the key is the path length
	result = []
	for dictionary in dict:
		for length in dictionary.values():
			result.append(length)
	return collections.Counter(result)

n = 1000
p = 1/60
G = nx.erdos_renyi_graph(n, p)

shortestPathDicts = list(nx.shortest_path_length(G).values())
print(shortestPathDicts)
length_dist = extract_length_distribution(shortestPathDicts)

print(length_dist)
print(length_dist.keys())
print(length_dist.values())

x = list(length_dist.keys())
y = list(length_dist.values())

x_pos = np.arange(len(x))
plt.bar(x_pos, y, align='center', alpha=0.5)
plt.xticks(x_pos, x)

plt.xlabel('Shortest Path Length')
plt.ylabel('Number of shortest paths')
#plt.plot(x, y)

#print(collections.Counter(nx.shortest_path_length(G)))

#nx.draw(G, node_size = [3 for v in G], with_labels = True)
plt.show()
