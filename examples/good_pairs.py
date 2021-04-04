import random

# This makes the import work even before package installation
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, "time_complexity"))

from time_complexity import plot_complexity


"""
Naive solution to the good pairs problem.
Time complexity is O(n^2).
"""
def pairs(nums):
    
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(n):

                if nums[i] == nums[j] and i < j:
                    count += 1
        
        return count


"""
Smarter solution to the good pairs problem.
Time complexity is O(n).
"""
def pairs2(nums):

    def get_triangular(n):
        if n <= 1:
            return 0
        else:
            return (n-1) + get_triangular(n-1)

    # Part 1: get count of each unique value
    n = len(nums)
    unique_counts = {}
    
    for i in range(n):

        if nums[i] not in unique_counts:
            unique_counts[nums[i]] = 1
            
        else:
            unique_counts[nums[i]] += 1
        
    # Part 2: find number of pairs for each value and count
    count = 0
    for e in unique_counts.values():
        count += get_triangular(e)
    
    return count


def generate_input(n):
    """
    Generator that creates input arguments with variable length
    for the function to be tested.
    Args:
        n (iterable): list of input lengths.
    Returns:
        Input arguments (tuple).
        i (int): length of input.
    Explicitly returning the length makes it compatible 
    wih functions with multiple arguments where 
    the length of only one arg is changed.
    """
    for i in n:
        yield ([random.randint(0, i//2) for _ in range(i)],), i


if __name__ == "__main__":

    # Note: you can use any kind of iterable for the inputs
    plot_complexity(pairs, generate_input(range(5, 100, 5)), repeat=1000)
