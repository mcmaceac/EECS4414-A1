#https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html
import itertools
import networkx as nx

def detectCommunities(G):
	k = 10	#stop after reaching greater than 10 communities
	comp = girvan_newman(G)
	limited = itertools.takewhile(lambda c: len(c) <= k, comp)
	for communities in limited:
		print(tuple(sorted(c) for c in communities))