from graphviz import Graph

# simple graph with manually designed edges

edges = [(3, 2),
         (3, 4),
         (2, 6),
         (3, 6),
         (2, 4),
         (2, 5),
         (1, 5),
         (4, 1)]

# save the graph
dot = Graph(comment='Graph 3 : Clique')
for edge in edges:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='cornflowerblue',
             penwidth='1.1')
graph_name = 'graphs/clique_5'
dot.render(graph_name)

clique = [2, 3, 4]
for node in clique:
    dot.node(str(node),
             color='crimson',
             penwidth='3.5')

# visualize the graph
graph_name = 'images/clique_5_highlight'
dot.render(graph_name)
