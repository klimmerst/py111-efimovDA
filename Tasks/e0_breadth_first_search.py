from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    buf_list = [start_node]
    final_list = [start_node]

    while len(buf_list) > 0:
        for i in g.neighbors(buf_list[0]):
            if i not in final_list:
                final_list.append(i)
                buf_list.append(i)
        buf_list.pop(0)
    return final_list
