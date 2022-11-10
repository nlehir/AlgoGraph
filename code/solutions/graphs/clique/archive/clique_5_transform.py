from graphviz import Graph

# simple graph with manually designed edges
edges = [{3, 2}, {3, 4}, {2, 6}, {3, 6}, {2, 4}, {2, 5}, {1, 5}, {4, 1}]


all_edges = [{i, j} for i in range(1, 7) for j in range(i + 1, 7)]
all_edges = [x for x in all_edges if len(x) > 1]
complementary_edges = [x for x in all_edges if x not in edges]

# save the graph
dot = Graph(comment="Graph 3 : Clique")
for edge in complementary_edges:
    edge = list(edge)
    dot.edge(str(edge[0]), str(edge[1]), color="forestgreen", penwidth="1.1")
graph_name = "graphs/clique_5_transform"
dot.render(graph_name)

clique = [2, 3, 4]
for node in clique:
    dot.node(str(node), color="crimson", penwidth="3.5")

# visualize the graph
graph_name = "images/clique_5_transform_highlight"
dot.render(graph_name)
