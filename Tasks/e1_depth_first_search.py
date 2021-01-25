from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """

    final_list = [start_node]
    buf_list = [start_node]

    while len(buf_list) > 0:
        for i in g.neighbors(buf_list[-1]):
            if i not in final_list:
                final_list.append(i)
                buf_list.append(i)
                break
        else:
            buf_list.pop(-1)

    return final_list
