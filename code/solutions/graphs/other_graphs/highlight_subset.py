from graphviz import Graph

# simple graph with manually designed edges
edges = [(1, 2),
         (3, 4),
         (4, 5),
         (5, 6),
         (2, 3),
         (6, 3),
         (6, 1),
         (1, 4),
         (2, 5),
         (1, 5)]

# save this simple graph
dot = Graph(comment='Graph 1 : dominating set')
for edge in edges:
    dot.edge(str(edge[0]),
             str(edge[1]),
             color='darkolivegreen4',
             penwidth='1.1')
graph_name = 'graphs/graph_1'
dot.render(graph_name)


# different subsets of nodes
# to see if they are dominating
sets = [[1],
        [3],
        [5, 2]]


def highlight_set(node_set, file_name, dot):
    # highlight the nodes in the subset
    for node in node_set:
        dot.node(str(node),
                 color='forestgreen',
                 penwidth='4')

    # visualize the graph
    graph_name = 'graphs/' + file_name
    dot.render(graph_name)


# generate several images
# one for each subset
for node_set in enumerate(sets):
        # if you dont know enumerate : it is useful to get the index
        # of the element in the list AND the element itself
        # recreate a new graph
    dot = Graph(comment='Graph 1 : dominating set')
    # plot the edges as usual
    for edge in edges:
        dot.edge(str(edge[0]),
                 str(edge[1]),
                 color='darkolivegreen4',
                 penwidth='1.1')
    file_name = 'graph_1_subset_' + str(node_set[0])
    highlight_set(node_set[1], file_name, dot)
