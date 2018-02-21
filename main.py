import networkx as nx 
import matplotlib.pyplot as plot 
from calc import computeGraphMeasurements

def showGraph(G):
	#show the graph itself
	nx.draw(G, node_size = [1 for v in G])
	plot.show()
	
def erdos_graphs():
	n = 10000
	p = 1/6
	fileName = "er1"
	G1 = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G1, fileName)
	
	p = 1/10
	fileName = "er2"
	G2 = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G2, fileName)
	
	p = 1/16
	fileName = "er3"
	G3 = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G3, fileName)
	
	p = 1/5
	fileName = "er4"
	G4 = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G4, fileName)
	
	p = 1/50
	fileName = "er5"
	G5 = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G5, fileName)
	
def watts_graphs():
	n = 10000
	k = 4		#Each node is connected to k nearest neighbors in ring topology
	p = 1/6		#Each node is connected to k nearest neighbours with probability p to rewire
	fileName = "ws1"
	G1 = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G1, fileName)
	
	p = 1/10
	k = 2
	fileName = "ws2"
	G2 = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G2, fileName)
	
	p = 1/16
	k = 200
	fileName = "ws3"
	G3 = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G3, fileName)
	
	p = 1/5
	k = 10
	fileName = "ws4"
	G4 = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G4, fileName)
	
	p = 1/50
	k = 20
	fileName = "ws5"
	G5 = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G5, fileName)
	
def barabasi_graphs():
	n = 10000

	m = 5 	#Number of edges to attach from a new node to existing nodes
	fileName = "ba1"
	G1 = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G1, fileName)
	
	m = 10
	fileName = "ba2"
	G2 = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G2, fileName)
	
	m = 20
	fileName = "ba3"
	G3 = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G3, fileName)
	
	m = 50
	fileName = "ba4"
	G4 = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G4, fileName)

	m = 2
	fileName = "ba5"
	G5 = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G5, fileName)
	

	
erdos_graphs()
watts_graphs()
barabasi_graphs()

