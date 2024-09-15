""""
    Build all paths arriving to destination
    avoiding loops
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
DESTINATION = 7

def plot_all_paths_to_dest(path_length, paths):
    number_of_paths = len(paths)
    for index, path in enumerate(paths):
        path_length = len(path)-1
        destination = path[-1]
        title = (
                f"Build all paths to {destination} without loops\n"
                f"Path {index+1}/{number_of_paths} of length {path_length}\n"
                f"{path}\n"
                f"Graph name: {GRAPH.name}"
                )
        fig_name = f"{GRAPH.name}_all_paths_to_{destination}_length_{path_length}_index_{index}_from_0_to_{destination}.pdf"
        folder = "all_paths_to_dest_no_loops"
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
    paths = [[[0]]]
    paths_to_destination, path_length = list(), 0

    while len(paths_to_destination) == 0:
        path_length += 1
        # build paths as before
        new_paths = list()
        for path in paths[path_length - 1]:
            for ngbr in GRAPH.neighbors(path[-1]):
                if ngbr not in path:
                    new_paths.append(path + [ngbr])

        # append the paths to the list of paths as before
        paths.append(new_paths)
        # check is the path goes to the destination
        paths_to_destination = [path for path in paths[path_length] if path[-1] == DESTINATION]

    plot_all_paths_to_dest(path_length=path_length, paths=paths_to_destination)

if __name__ == "__main__":
    main()
