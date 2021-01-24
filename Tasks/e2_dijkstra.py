from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    final_dict = {}
    for i in g.nodes:
        final_dict[i] = float("inf")
    visited_nodes = [starting_node]
    final_dict[starting_node] = 0
    c = 0
    while len(visited_nodes) > 0:
        for i in g.neighbors(visited_nodes[0]):
            if i not in visited_nodes:
                if final_dict[i] > g[visited_nodes[0]][i]['weight'] + final_dict[visited_nodes[0]]:
                    final_dict[i] = g[visited_nodes[0]][i]['weight'] + final_dict[visited_nodes[0]]
                    visited_nodes.append(i)
        visited_nodes.pop(0)
    return final_dict