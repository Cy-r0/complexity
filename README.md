# time_complexity

Measure time complexity of python functions.


## How to install

Install package with pip:

    ```
    python -m pip install git+https://github.com/Cy-r0/time_complexity#egg=time_complexity
    ```


## How to use

1. Put the code you want to time inside a function, for example:

    ```python
    def append(mylist, num):
        return mylist.append(num)
    ```


2. Create an iterable or iterator that yields the arguments of the function for all input lengths you're interested in, e.g.:
  
    ```python
    import random

    def generate_input(start, stop, step):
        for n in range(start, stop, step):
            mylist = [random.randint(0, n) for _ in range(n)]
            num = 3
            yield (mylist, num), n
    ```

    The above generator returns a tuple of two things:

    1. The arguments of your function (i.e. mylist and num)
    2. The length of the argument you're changing

    You can also put all this data in a list or any other iterable.


3. Call ```plot_complexity()``` like below:

    ```python
    from time_complexity import plot_complexity

    plot_complexity(append_to_list, generate_input(0, 100, 5))
    ```

    You can optionally specify a third argument, ```repeat``` (defaults to 1000), which defines how many times execution is repeated to obtain a reasonable approximation for the real execution time (remember, execution time depends on many factors like CPU capabilities, what else is the CPU busy with..., so the time measurement can have a high variance).

    The function will output the below:

    ```
    Plot complexity. Repeat: 1000
    Iterating over input lengths...
    Input len: 0 	Time: 0.154 us
    Input len: 5 	Time: 0.145 us
    Input len: 10 	Time: 0.15199 us
    Input len: 15 	Time: 0.145 us
    Input len: 20 	Time: 0.149 us
    Input len: 25 	Time: 0.142 us
    Input len: 30 	Time: 0.148 us
    Input len: 35 	Time: 0.145 us
    Input len: 40 	Time: 0.144 us
    Input len: 45 	Time: 0.157 us
    Input len: 50 	Time: 0.144 us
    Input len: 55 	Time: 0.146 us
    Input len: 60 	Time: 0.144 us
    Input len: 65 	Time: 0.143 us
    Input len: 70 	Time: 0.143 us
    Input len: 75 	Time: 0.14999 us
    Input len: 80 	Time: 0.156 us
    Input len: 85 	Time: 0.151 us
    Input len: 90 	Time: 0.149 us
    Input len: 95 	Time: 0.14999 us

    ```

    And a plot will appear:

    ![constant_time](media/O(1).png)

    There is no correlation between input length and time, which suggests complexity is O(1).

    For another example, check out ```examples/max.py```, where an O(n) algorithm is timed. Plot is below:

    ![quad_time](media/O(n).png)

