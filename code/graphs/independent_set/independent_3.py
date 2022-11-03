from graphviz import Graph

# simple graph with manually designed edges
edges = [
    (7, 2),
    (3, 4),
    (4, 5),
    (5, 6),
    (8, 3),
    (6, 3),
    (1, 8),
    (6, 1),
    (7, 4),
    (2, 5),
    (10, 5),
    (10, 4),
    (1, 5),
    (6, 2),
    (5, 7),
    (9, 8),
]


# save the graph
dot = Graph(comment="Graph 1 : Independent set")
for edge in edges:
    dot.edge(str(edge[0]), str(edge[1]), color="black", penwidth="1.1")
graph_name = "graphs/independent_set_0"
dot.render(graph_name)

indep_set = [1, 3, 10, 2, 9]
for node in indep_set:
    dot.node(str(node), color="aquamarine4", penwidth="3.5")

# visualize the graph
graph_name = "graphs/independent_set_3"
dot.render(graph_name)
