import networkx as nx
from utils import plot_initial_graph

neighbors = {
        0:[1, 3, 4],  # neighbors of 0
        1:[0, 2, 3],  # neighbors of 1
        2:[1, 5],  # neighbors of 2
        3:[0, 1, 5],  # neighbors of 3
        4:[0],  # neighbors of 4
        5:[2, 3],
}

G = nx.from_dict_of_lists(d=neighbors)
G.name = "G"
pos = plot_initial_graph(
        G=G,
        name="G",
        )

neighbors_2 = {
        0:[1, 3, 4],  # neighbors of 0
        1:[0, 2, 3],  # neighbors of 1
        2:[1, 5],  # neighbors of 2
        3:[0, 1, 5, 6],  # neighbors of 3
        4:[0, 6],  # neighbors of 4
        5:[2, 3, 6],  # neighbors of 5
        6:[4, 5, 3, 7],  # neighbors of 6
        7:[6], # neighbors of 7
    }

G2 = nx.from_dict_of_lists(d=neighbors_2)
G2.name = "G2"
pos2 = plot_initial_graph(
        G=G2,
        name="G2",
        )
