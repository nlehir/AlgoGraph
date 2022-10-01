from graphviz import Graph

# simple graph with manually designed edges
edges = [(1, 2),
         (3, 4),
         (4, 5),
         (5, 6),
         (2, 3),
         (6, 3),
         (4, 8),
         (6, 1),
         (1, 4),
         (2, 5),
         (1, 5),
         (5, 7),
         (2, 8)]

color_1 = [1, 8]
color_2 = [3, 5]
color_3 = [4, 7]
color_4 = [2, 6]
coloring = [(color_1, 'darkorchid4'),
            (color_2, 'aquamarine4'),
            (color_3, 'goldenrod3'),
            (color_4, 'orange')]

# colors = ['black', 'aquamarine4', 'goldenrod3', 'darkorchid4']

# save this simple graph
dot = Graph(comment='Graph 1 : graph to color')
for edge in edges:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='black',
             penwidth='1.1')
graph_name = 'graphs/coloring_0'
dot.render(graph_name)


def color_set(node_set, color, dot):
    for node in node_set:
        dot.node(str(node),
                 color=color,
                 penwidth='2')


for color in coloring:
    node_set = color[0]
    color = color[1]
    color_set(node_set, color, dot)

# visualize the graph
graph_name = 'graphs/coloring_3'
dot.render(graph_name)
