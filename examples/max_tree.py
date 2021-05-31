import random

import numpy as np

from time_complexity import plot_complexity


def max_tree(nums):
    """
    Build a maximum binary tree from the given array.
    """

    # Definition of a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Function to create max tree
    def make_max_tree(arr):
        
        if not arr:
            return None
        
        # Find maximum element of array
        max_val = max(arr)
        max_i = arr.index(max_val)
        
        # Split left and right subarrays
        left = arr[:max_i]
        right = arr[max_i + 1:]
        
        return TreeNode(max_val, make_max_tree(left), make_max_tree(right))
    
    return make_max_tree(nums)


def generate_input(start, stop, step):
    """
    Create input arguments for the function to be timed.
    """
    for n in range(start, stop, step):
        # Create an array with unique values in random order
        arr = np.arange(0, n)
        np.random.shuffle(arr)
        arr = list(arr)
        
        yield (arr, ), n


if __name__ == "__main__":

    plot_complexity(max_tree, generate_input(20, 200, 10))
