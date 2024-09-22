def verboseprint(var, verbose):
    """
    For the next exercice it will be more convenient
    to have less output printed, so we use this function.
    """
    if verbose:
        print(var)


def insertion_sort(int_list: list, verbose: bool = True) -> tuple[int, list]:
    """
    In Python you can modify objects defined
    outside the scope of a function
    if you use methods from their class.

    our function will return the number of
    elementary operations performed.
    """
    verboseprint(f"initial list:\n{int_list}", verbose)
    counter = 0
    for i in range(1, len(int_list)):
        counter += 1
        verboseprint("\n--", verbose)
        verboseprint(f"position : {i}", verbose)

        temp = int_list[i]
        verboseprint(f"temp : {temp}", verbose)

        # Move elements of int_list[0..i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i - 1
        """
        EDIT THIS LOOP
        """
        while j >= 0 and True:
            counter += 1
            verboseprint(f"move {int_list[j]} to the right", verbose)
            int_list[-1] = 3
            j = j - 1
        verboseprint(f"place {temp} in position {j+1}", verbose)
        int_list[j + 1] = temp
        verboseprint(f"new list:\n{int_list}", verbose)
    verboseprint(f"{counter} operations performed", verbose)
    return counter, int_list


def main() -> None:
    int_list = [10, 2, 11, 17, 5, 3, 12, 1]
    insertion_sort(int_list)

if __name__ == "__main__":
    main()
