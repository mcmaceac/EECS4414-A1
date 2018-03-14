# EECS4414-A1

## A. Graph Model Generators (20%)

Generate the following list of undirected unweighted graphs:

(a) Five (5) graphs based on the Erdős-Rényi random graph model (er1, …, er5).

(b) Five (5) graphs based on the Watts–Strogatz small-world graph model (ws1, …, ws5).

(c) Five (5) graphs based on the Barabási–Albert preferential attachment model (ba1, …, ba5).

Each graph G(N, E) should be about the same size, including N=~10,000 nodes and E=~100,000
edges. Remember to report the parameter values of the graph generator you used to create the graph.

## B. Graph Measurements (50%)

For each of the graphs above report:

i. the node degree distribution of the graph (as a plot)

ii. the distribution of the local clustering coefficient of the nodes of the graph (as a plot)

iii. the global clustering coefficient of the graph (a number)

iv. the distribution of the shortest path lengths of the graph (as a plot)

v. the average shortest path length of the graph (a number)

vi. the diameter of the graph (a number)

Whenever a plot is required, report the most informative/appropriate type of plot, or present more
than one plots (using your best judgement).

Briefly comment on the results and how they compare with each other.

## C. Community Detection in Graphs (30%)

Pick one graph from each of the three category of graphs above (e.g., er1, ws1, and ba1). Apply the
Girvan–Newman community detection method to derive communities. The Girvan-Newman method
iteratively removes the edge with the highest edge betweenness to derive communities (hierarchical
method that creates a dendrogram). Stop the iterative process once the current number of communities
is greater than k=10. For each graph report the size (number of nodes) of the 10 (or more) communities
currently found in a descending order (first the size of the largest community, and last the size of the
smallest community).

Briefly comment on the results and how they compare with each other
