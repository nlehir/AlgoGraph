from graphviz import Graph

# simple graph with manually designed edges
subset_1 = [1, 2, 3, 4, 5, 6]
subset_2 = [7, 8, 9, 10, 11, 12]

edges = []
for node_1 in subset_1:
    for node_2 in subset_2:
        edges.append((node_1, node_2))

# save this simple graph
dot = Graph(comment='Graph 1 : bipartite graph')
for edge in edges:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='darkolivegreen4',
             penwidth='1.1')
graph_name = 'graphs/bipartite'
dot.render(graph_name)
