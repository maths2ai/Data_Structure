# A* 

The A* algorithm tries to solve the problem of finding the "best path" to connect two nodes inside a graph.
Edges for moving from a node "alpha" to a node "beta" are computed via Euclidean norm.

A* works in a similar way to Dijkstra algorithm. At each step it considers the closest node to the "goal node" amongst the nodes that are reachable from the starting node. Let's denote the rachable nodes with "R". To evaluate the distance from each reachable node to the "goal node" A* uses an approximation: "the as crow flies" distance between the nodes in "R" and the goal node.
It then constructs the "best path" adding the edge that links the starting node to the node in "R" that has the smallest approximate distance form the goal node.
A* iterates this approach till solution.
