from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    nodes, queue = [start_node], [start_node]

    for item in queue:
        for node in g.neighbors(item):
            if node not in nodes:
                nodes.append(node)
                queue.append(node)
    queue.pop(0)

    return nodes


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
    ('A', 'F'),
    ('B', 'G'),
    ('F', 'G'),
    ('G', 'C'),
    ('G', 'H'),
    ('G', 'I'),
    ('C', 'H'),
    ('I', 'H'),
    ('H', 'D'),
    ('H', 'E'),
    ('H', 'J'),
    ('E', 'D'),
    ])
    print(bfs(graph, 'A'))
