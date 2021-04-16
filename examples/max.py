import random

from time_complexity import plot_complexity


def find_max(l):
    """
    Return maximum element of list. Complexity is O(n).
    """
    return max(l)


def generate_input(start, stop, step):
    """
    Create input arguments for the function to be timed.
    """
    for n in range(start, stop, step):
        l = [random.randint(0, n) for _ in range(n)]
        yield (l, ), n


if __name__ == "__main__":

    plot_complexity(find_max, generate_input(500, 10000, 500))
