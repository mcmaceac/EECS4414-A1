import networkx as nx 
import matplotlib.pyplot as plot 
import numpy as np
import sys 
import re
import collections
import time
import datetime

def extract_length_distribution(G):
	#this function extracts the lengths of all shortest paths and returns it as a dictionary
	#where the key is the path length and the value if the number of paths of that length in G
	lengths = []
	for splTuple in nx.shortest_path_length(G):
		for len in splTuple[1].values():
			lengths.append(len)
	return collections.Counter(lengths)


def computeGraphMeasurements(G, fileName):

	saveGraph(G, fileName)
	degreeDistribution(G, fileName)
	clusteringDistribution(G, fileName)
	splDistribution(G, fileName)

	print("[" + getTimeStamp() + "]" + "Starting txt file data for " + fileName + "...")
	file = open(fileName + "/" + fileName + "_data.txt", "w")
	#B part iii
	#print("Global clustering coefficient: %s" % nx.average_clustering(G))
	file.write("Global clustering coefficient: %s\n" % nx.average_clustering(G))

	#B part v
	#print("Average shortest path length: %s" % nx.average_shortest_path_length(G))
	file.write("Average shortest path length: %s\n" % nx.average_shortest_path_length(G))

	#B part vi
	#print("Diameter of the graph: %s" % nx.diameter(G))
	file.write("Diameter of the graph: %s\n" % nx.diameter(G))
	file.close()
	print("[" + getTimeStamp() + "]" + "Finished txt file data for " + fileName + "...")
	
def saveGraph(G, fileName):
	#storing the adjacency list of the generated graph for later use
	fh = open(fileName + "/" + fileName + ".adjlist", "wb")
	nx.write_adjlist(G, fh)
	fh.close()
	
def degreeDistribution(G, fileName):
	print("[" + getTimeStamp() + "]" + "Starting degree distribution for " + fileName + "...")
	#B part i
	i = nx.degree_histogram(G)		#A list of frequencies of degrees. The degree values are the index in the list.
	plot.ylabel('Frequency')
	plot.xlabel('Node degree')
	plot.plot(i)
	#plot.show()			#only needed for on demand testing
	plot.savefig(fileName + "/" + fileName + "_degree_dist.pdf")
	plot.close()
	print("[" + getTimeStamp() + "]" + "Finished degree distribution for " + fileName)
	
def clusteringDistribution(G, fileName):
	print("[" + getTimeStamp() + "]" + "Starting clustering distribution for " + fileName + "...")
	#B part ii
	clust = nx.clustering(G)
	x = list(clust.keys())
	y = list(clust.values())
	plot.ylabel('Clustering Coefficient')
	plot.xlabel('Node Number')
	x_pos = np.arange(len(x))
	plot.bar(x_pos, y, align='center', alpha=0.5)
	#plot.show()
	plot.savefig(fileName + "/" + fileName + "_clust_dist.pdf")
	plot.close()
	print("[" + getTimeStamp() + "]" + "Finished clustering distribution for " + fileName)
	
def splDistribution(G, fileName):
	print("[" + getTimeStamp() + "]" + "Starting shortest path distribution for " + fileName + "...")
	#B part iv
	length_dist = extract_length_distribution(G)
	x = list(length_dist.keys())
	y = list(length_dist.values())
	plot.xlabel('Shortest Path Length')
	plot.ylabel('Number of shortest paths')
	x_pos = np.arange(len(x))
	plot.bar(x_pos, y, align='center', alpha=0.5)
	plot.xticks(x_pos, x)
	#plot.show()
	plot.savefig(fileName + "/" + fileName + "_spl_dist.pdf")
	plot.close()
	print("[" + getTimeStamp() + "]" + "Finished shortest path distribution for " + fileName)

def getTimeStamp():
	ts = time.time()
	return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')