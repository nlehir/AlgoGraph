""""
    Build all the paths from 0
"""

from input_graphs import G, pos, G2, pos2

from utils import highlight_path

"""
Choose the graph to process
"""
GRAPH = G2
POS = pos2
# GRAPH = G
# POS = pos

def plot_all_paths(path_length, paths):
    number_of_paths = len(paths)
    for index, path in enumerate(paths):
        path_length = len(path)-1
        destination = path[-1]
        title = (
                "Build all paths\n"
                f"Path {index+1}/{number_of_paths} of length {path_length}\n"
                f"From 0 to {destination}: {path}\n"
                f"Graph name: {GRAPH.name}"
                )
        fig_name = f"{GRAPH.name}_all_paths_length_{path_length}_index_{index}_from_0_to_{destination}.pdf"
        folder = "all_paths"
        print(path)
        highlight_path(
                G=GRAPH,
                path=path,
                pos=POS,
                title=title,
                fig_name=fig_name,
                folder=folder,
                )

def main():
    # paths of length 0
    # a path will be coded as a list
    # we will have a list of paths lengths
    # each path length corresponds to a list
    # so we have a list of lists of lists
    paths = [[[0]]]
    number_of_nodes = len(GRAPH)

    for path_length in range(1, number_of_nodes):
        print(f"building paths of length {path_length}")
        new_paths = list()
        """
        EDIT: add lines here
        """
        for path in paths[path_length - 1]:
            pass
        paths.append(new_paths)


    print(f"paths of length 1 : {paths[1]}")
    print(f"paths of length 2 : {paths[2]}")
    print(f"paths of length 4 : {paths[4]}")

    for path_length in range(1, 5):
        plot_all_paths(path_length=path_length, paths=paths[path_length])

if __name__ == "__main__":
    main()
