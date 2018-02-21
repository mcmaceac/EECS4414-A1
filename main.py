import networkx as nx 

from calc import computeGraphMeasurements

n = 1000
p = 1/6
G = nx.erdos_renyi_graph(n, p)

computeGraphMeasurements(G)