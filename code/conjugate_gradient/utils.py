from termcolor import colored
import pickle
import os


def print_colored(
    text: str,
    color="green",
) -> None:
    colored_text = colored(
        text,
        color=color,
        attrs=["bold"],
    )
    print(colored_text)


def clean_filename(name: str) -> str:
    name = name.replace(".", "_")
    name = name.replace(" ", "_")
    return name


def save_pickle(data, file_path: str) -> None:
    with open(file_path, "wb") as handle:
        pickle.dump(data, handle)

def load_pickle(file_path: str) -> None:
    with open(file_path, "rb") as handle:
        data = pickle.load(handle)
    return data

def create_folder_if_missing(folder) -> None:
    if not os.path.exists(folder):
        os.makedirs(folder)
