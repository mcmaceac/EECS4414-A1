#https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html
import itertools
import networkx as nx
import matplotlib.pyplot as plot 
from networkx.algorithms.community.centrality import girvan_newman

def detectCommunities(G, fileName):
	communitySizes = []
	k = 10	#stop after reaching greater than 10 communities
	comp = girvan_newman(G)
	limited = itertools.takewhile(lambda c: len(c) <= k, comp)
	for communities in limited:
		if len(communities) == k:	
			#print(communities)
			for community in communities:
				#print(len(community))
				communitySizes.append(len(community))
	saveCommunities(sorted(communitySizes, reverse=True), fileName)

def saveCommunities(communityLengths, fileName):
	file = open(fileName + "/" + fileName + "_communities.txt", "w")
	file.write(communityLengths)
	file.close()

fileName = "er1"
fh = open(fileName + "/" + fileName + ".adjlist", "rb")
G = nx.read_adjlist(fh)
print(fileName + " loaded")
fh.close()
detectCommunities(G, fileName)

fileName = "ws1"
fh = open(fileName + "/" + fileName + ".adjlist", "rb")
G = nx.read_adjlist(fh)
print(fileName + " loaded")
fh.close()
detectCommunities(G, fileName)

fileName = "ba1"
fh = open(fileName + "/" + fileName + ".adjlist", "rb")
G = nx.read_adjlist(fh)
print(fileName + " loaded")
fh.close()
detectCommunities(G, fileName)