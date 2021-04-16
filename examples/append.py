import random

from time_complexity import plot_complexity


def append(mylist, num):
    """
    Append number to list. Complexity is O(1).
    """
    return mylist.append(num)


def generate_input(start, stop, step):
    """
    Create input arguments for the function to be timed.
    In this case, for the function list_append() there are two args: (l, num).
    l changes in complexity (length), while num stays the same.
    Depending on your needs, you can add other arguments.
    """
    for n in range(start, stop, step):
        mylist = [random.randint(0, n) for _ in range(n)]
        num = 3
        yield (mylist, num), n


if __name__ == "__main__":

    plot_complexity(append, generate_input(0, 100, 5))
