## TODO
"""
Dijkstra’s Algorithm
    algorithm for traversing or searching graphs

    use examples:
    1) shortest path between two nodes (weighted, undirected graph, like cities and routes on the map)
"""
"""
Algorithm for Dijkstra’s Algorithm:
Mark the source node with a current distance of 0 and the rest with infinity.
Set the non-visited node with the smallest current distance as the current node.
For each neighbor, N of the current node adds the current distance of the adjacent node with the weight of the edge connecting 0->1. If it is smaller than the current distance of Node, set it as the new current distance of N.
Mark the current node 1 as visited.
Go to step 2 if there are any nodes are unvisited.
"""

