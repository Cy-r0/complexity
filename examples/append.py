import random

# This makes the import work even before package installation
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, "time_complexity"))

from time_complexity import plot_complexity


"""
Append one number to a list. Complexity is O(1).
"""
def append_to_list(mylist, num):
    return mylist.append(num)


def generate_input():
    for l in range(30):
        mylist = [random.randint(0, 3) for _ in range(l)]
        num = 3
        yield (mylist, num), l


if __name__ == "__main__":

    plot_complexity(append_to_list, generate_input())
