def verboseprint(var, verbose: bool = False) -> None:
    """
    For the next exercice it will be more convenient
    to have less output printed, so we use this function.
    """
    if verbose:
        print(var)


def insertion_sort(llist: list, verbose: bool = True) -> int:
    """
    In Python you can modify objects defined
    outside the scope of a function
    if you use methods from their class.

    Our function will return the number of
    elementary operations performed.
    """
    verboseprint(f"initial list:\n{llist}", verbose)
    counter = 0
    for i in range(1, len(llist)):
        verboseprint("\n--", verbose)
        verboseprint(f"position : {i}", verbose)

        temp = llist[i]
        verboseprint(f"temp : {temp}", verbose)

        # Move elements of llist[0..i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and temp < llist[j]:
            verboseprint(f"move {llist[j]} to the right", verbose)
            llist[j + 1] = llist[j]
            counter += 1
            j = j - 1
        verboseprint(f"place {temp} in position {j+1}", verbose)
        llist[j + 1] = temp
        counter += 1
        verboseprint(f"new list:\n{llist}", verbose)
    verboseprint(f"{counter} operations performed", verbose)
    return counter



def main() -> None:
    llist = [10, 2, 11, 17, 5, 3, 12, 1]
    insertion_sort(llist)

if __name__ == "__main__":
    main()
