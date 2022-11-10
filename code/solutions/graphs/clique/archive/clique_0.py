from graphviz import Graph

# simple graph with manually designed edges
edges = [
    (7, 2),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (8, 3),
    (6, 3),
    (2, 4),
    (1, 8),
    (6, 1),
    (7, 11),
    (7, 4),
    (2, 5),
    (10, 5),
    (10, 4),
    (1, 5),
    (4, 11),
    (10, 11),
    (6, 2),
    (5, 7),
    (9, 8),
]


# save the graph
dot = Graph(comment="Graph 0 : Clique")
for edge in edges:
    dot.edge(str(edge[0]), str(edge[1]), color="cornflowerblue", penwidth="1.1")
graph_name = "graphs/clique_0"
dot.render(graph_name)

# visualize the graph
graph_name = "images/clique_0"
dot.render(graph_name)
