import matplotlib.pyplot as plt
import collections
import numpy as np

from igraph import *

def extract_length_distribution(G):
	return collections.Counter(lengthList(G))

def splDistribution(G, fileName): 
	print("Starting spl dist for " + fileName + "...")
	#print(G.shortest_paths())
	splDist = extract_length_distribution(G)

	#print(list(splDist.keys()))
	#print(list(splDist.values()))

	x = list(splDist.keys())
	y = list(splDist.values())
	plt.xlabel("Shortest path length")
	plt.ylabel("Frequency")
	#x_pos = np.arange(len(x))
	plt.bar(x, y, align='center')
	plt.xticks(x)
	#plt.show()
	plt.savefig(fileName + "/" + fileName + "_spl_dist.png")
	plt.close()
	print("Finished!")

def degreeDistribution(G, fileName):
	print("Starting degree dist for " + fileName + "...")
	degreeDist = collections.Counter(G.degree())
	x = list(degreeDist.keys())
	y = list(degreeDist.values())
	plt.xlabel("Degree")
	plt.ylabel("Frequency")
	plt.bar(x, y, align='center')
	#plt.xticks(x)
	#print(degreeDist)
	#plt.show()
	plt.savefig(fileName + "/" + fileName + "_degree_dist.png")
	plt.close()
	print("Finished!")

def clusteringDistribution(G, fileName):
	print("Starting clustering dist for " + fileName + "...")
	clustDist = G.transitivity_local_undirected()
	#print(clustDist)
	plt.xlabel("Node number")
	plt.ylabel("Clustering coefficient")
	x = list(range(0, len(clustDist)))
	plt.bar(x, clustDist, align='center', alpha=0.5)
	#plt.show()
	plt.savefig(fileName + "/" + fileName + "_clust_dist.png")
	plt.close()
	print("Finished!")

def globalClustering(G):
	gClust = G.transitivity_undirected()
	#print(gClust)
	return gClust

def averageShortestPath(G):
	pathLengths = lengthList(G)
	average = sum(pathLengths) / float(len(pathLengths))
	#print(average)
	return average

def lengthList(G):
	pathLengths = []
	for subArray in G.shortest_paths():
		for spl in subArray:
			if spl != float('Inf'):	#filtering non-reachable nodes
				pathLengths.append(spl)
	return pathLengths

def graphDiameter(G):
	return G.diameter()

def computeGraphMeasurements(G, fileName):
	#degreeDistribution(G, fileName)
	clusteringDistribution(G, fileName)
	'''
	splDistribution(G, fileName)

	print("Writing data to text file for " + fileName)
	file = open(fileName + "/" + fileName + "_data.txt", "w")
	file.write("Global clustering coefficient: %s\n" % globalClustering(G))
	file.write("Average shortest path length: %s\n" % averageShortestPath(G))
	file.write("Diameter of the graph: %s\n" % graphDiameter(G))
	print("Finished!")
	'''
#print(G.degree())
#print(G.transitivity_local_undirected())
#splDistribution(G)
#degreeDistribution(G)
#clusteringDistribution(G)
#globalClustering(G)
#averageShortestPath(G)
#graphDiameter(G)






