# A* 

In this project we are going to solve the problem of finding the "best path" to connect two nodes inside a graph.
Edges that represent the cost for moving from a node "alpha" to a node "beta" are computed via Euclidean norm.

The solution provided is A*. A* works in a similar way to Dijkstra algorithm. At each step it considers the node closest to the "goal node", amongst those reachable from the starting node, to
