from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    path_costs = {i: float('inf') for i in g.nodes()}
    path_costs[starting_node] = 0
    queue, visited = [starting_node], [starting_node]

    while queue:
        for node in g.neighbors(queue[0]):
            path = path_costs[queue[0]] + g.edges()[queue[0], node]['weight']
            if path < path_costs[node]:
                path_costs[node] = path
            if node not in visited:
                queue.append(node)
        if queue[0] not in visited:
            visited.append(queue[0])
        queue.pop(0)

    return path_costs


if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_weighted_edges_from([
            ("A", "B", 1),
            ("B", "C", 3),
            ("C", "E", 4),
            ("E", "F", 3),
            ("B", "E", 8),
            ("C", "D", 1),
            ("D", "E", 2),
            ("B", "D", 2),
            ("G", "D", 1),
            ("D", "A", 2),
        ])

    print(dijkstra_algo(graph, 'A'))
