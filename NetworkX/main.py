import networkx as nx 
import matplotlib.pyplot as plot 
from calc import computeGraphMeasurements

def showGraph(G):
	#show the graph itself
	nx.draw(G, node_size = [1 for v in G])
	plot.show()
	
def erdos_graphs():
	n = 1000
	
	p = 1/6
	fileName = "er1"
	print("Generating graph " + fileName)
	G = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/2
	fileName = "er2"
	print("Generating graph " + fileName)
	G = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/16
	fileName = "er3"
	print("Generating graph " + fileName)
	G = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/5
	fileName = "er4"
	print("Generating graph " + fileName)
	G = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G, fileName)
	
	
	p = 1/6
	fileName = "er5"
	print("Generating graph " + fileName)
	G = nx.erdos_renyi_graph(n, p)
	computeGraphMeasurements(G, fileName)
	
def watts_graphs():
	n = 10000
	k = 4		#Each node is connected to k nearest neighbors in ring topology
	p = 1/6		#Each node is connected to k nearest neighbours with probability p to rewire
	fileName = "ws1"
	G = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/10
	k = 2
	fileName = "ws2"
	G = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/16
	k = 200
	fileName = "ws3"
	G = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/5
	k = 10
	fileName = "ws4"
	G = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G, fileName)
	
	p = 1/50
	k = 20
	fileName = "ws5"
	G = nx.watts_strogatz_graph(n, k, p)
	computeGraphMeasurements(G, fileName)
	
def barabasi_graphs():
	n = 10000

	m = 5 	#Number of edges to attach from a new node to existing nodes
	fileName = "ba1"
	G = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G, fileName)
	
	m = 10
	fileName = "ba2"
	G = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G, fileName)
	
	m = 20
	fileName = "ba3"
	G = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G, fileName)
	
	m = 50
	fileName = "ba4"
	G = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G, fileName)

	m = 2
	fileName = "ba5"
	G = nx.barabasi_albert_graph(n, m)
	computeGraphMeasurements(G, fileName)
	

	
erdos_graphs()
watts_graphs()
barabasi_graphs()

