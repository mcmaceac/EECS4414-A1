import networkx as nx 
import matplotlib.pyplot as plot 

def showGraph(G):
	#show the graph itself
	nx.draw(G, node_size = [3 for v in G])
	plot.show()

from calc import computeGraphMeasurements

n = 10000		#Number of nodes
p = 1/6
k = 4		#Each node is connected to k nearest neighbors in ring topology
m = 4		#Number of edges to attach from a new node to existing nodes

#G = nx.erdos_renyi_graph(n, p)

#Each node is connected to k nearest neighbours with probability p to rewire
G = nx.watts_strogatz_graph(n, k, p)

#G = nx.barabasi_albert_graph(n, m)

showGraph(G)
#computeGraphMeasurements(G)

