"""
Breadth First Search     time complexity O(|V| + |E|) - V - number of nodes, E - number of edges
    algorithm for traversing or searching graphs

    use examples:
    1) shortest path between two nodes (unweighted graph)
"""


def bfs_find_shortest_path(graph: dict, start_node: str, end_node: str) -> list[str]:
    """
    use backtracking to find a shortest path between two nodes in a graph.

    :param graph: dict
    :param start_node: str
    :param end_node: str
    :rtype str
    """
    if not graph:
        return []
    visited_nodes = []
    nodes_queue = [start_node]
    predecessor_nodes = {}
    while nodes_queue:
        current_node = nodes_queue.pop(0)
        visited_nodes.append(current_node)
        for neighbour in graph.get(current_node):
            if neighbour not in visited_nodes:
                nodes_queue.append(neighbour)
                predecessor_nodes[neighbour] = current_node
    return shortest_path(predecessor_nodes, start_node, end_node)


def shortest_path(predecessor_node, start_node, end_node):
    path = [end_node]
    current_node = end_node
    while current_node != start_node:
        current_node = predecessor_node[current_node]
        path.append(current_node)
    path.reverse()
    return path


if __name__ == '__main__':
    graph_example = {
        "0": ["9", "3", "5"],
        "1": ["6", "7", "4"],
        "2": ["5", "10"],
        "3": ["0"],
        "4": ["1", "5", "8"],
        "5": ["2", "0", "4"],
        "6": ["1"],
        "7": ["1"],
        "8": ["4"],
        "9": ["0"],
        "10": ["2"],
    }
    shortest_path = bfs_find_shortest_path(graph_example, '0', '1')
    print(shortest_path)
