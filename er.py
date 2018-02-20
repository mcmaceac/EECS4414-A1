import networkx as nx 
import matplotlib.pyplot as plot 
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
p = 1/6
G = nx.erdos_renyi_graph(n, p)

#B part i
i = nx.degree_histogram(G)
plot.ylabel('Node Degree')
plot.xlabel('Frequency')
plot.plot(i)
plot.show()

#B part ii
clust = nx.clustering(G)
x = list(clust.keys())
y = list(clust.values())
plot.ylabel('Clustering Coefficient')
plot.xlabel('Node Number')
plot.plot(x, y)
plot.show()

#B part iii
print("Global clustering coefficient: %s" % nx.average_clustering(G))

#B part iv
shortestPathDicts = list(nx.shortest_path_length(G).values())
length_dist = extract_length_distribution(shortestPathDicts)
x = list(length_dist.keys())
y = list(length_dist.values())
plot.xlabel('Shortest Path Length')
plot.ylabel('Number of shortest paths')
x_pos = np.arange(len(x))
plot.bar(x_pos, y, align='center', alpha=0.5)
plot.xticks(x_pos, x)
plot.show()

#B part v
print("Average shortest path length: %s" % nx.average_shortest_path_length(G))

#B part vi
print("Diameter of the graph: %s" % nx.diameter(G))