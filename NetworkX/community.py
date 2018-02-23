#https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html
import itertools
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman

def detectCommunities(G):
	k = 2	#stop after reaching greater than 10 communities
	comp = girvan_newman(G)
	limited = itertools.takewhile(lambda c: len(c) <= k, comp)
	for communities in limited:
		print(tuple(sorted(c) for c in communities))

n = 100
p = 1/6
G = nx.erdos_renyi_graph(n, p)
detectCommunities(G)