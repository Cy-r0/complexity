# time_complexity

Measure time complexity of python functions.


## How to install

- Install package with pip:

```
python -m pip install git+https://github.com/Cy-r0/time_complexity#egg=time_complexity
```


## How to use

- Put your code inside a function, for example:

```python
def append_to_list(mylist, num):
    return mylist.append(num)
```
- Create an iterable or iterator that contains the arguments of the function for all input lengths you're interested in, e.g.:
  
```python
import random

def generate_input():
    for l in range(30):
        mylist = [random.randint(0, 3) for _ in range(l)]
        num = 3
        yield (mylist, num), l
```

This generator returns a tuple of two things:

1. The arguments of your function (i.e. mylist and num)
2. The length of the argument you're changing (in this example, you're changing the length of mylist from 0 to 29 elements)

You can also put all this data in a list or any other iterable.

- Call ```plot_complexity()``` like below:

```python
from time_complexity import plot_complexity

plot_complexity(append_to_list, generate_input())
```

You can optionally specify a third argument, ```repeat``` (defaults to 1000), which defines how many times execution is repeated to obtain a reasonable approximation for the real execution time (remember, execution time depends on many factors like CPU capabilities, what else is the CPU busy with..., so the time measurement can have a high variance).

The function will output the below:

```
Plot complexity. Repeat: 1000
Iterating over input lengths...
Input len: 0 	Time: 0.16 us
Input len: 1 	Time: 0.141 us
Input len: 2 	Time: 0.159 us
Input len: 3 	Time: 0.146 us
Input len: 4 	Time: 0.146 us
Input len: 5 	Time: 0.159 us
Input len: 6 	Time: 0.159 us
Input len: 7 	Time: 0.16 us
Input len: 8 	Time: 0.14 us
Input len: 9 	Time: 0.141 us
Input len: 10 	Time: 0.141 us
Input len: 11 	Time: 0.141 us
Input len: 12 	Time: 0.142 us
Input len: 13 	Time: 0.144 us
Input len: 14 	Time: 0.141 us
Input len: 15 	Time: 0.142 us
Input len: 16 	Time: 0.147 us
Input len: 17 	Time: 0.159 us
Input len: 18 	Time: 0.159 us
Input len: 19 	Time: 0.139 us
Input len: 20 	Time: 0.158 us
Input len: 21 	Time: 0.143 us
Input len: 22 	Time: 0.14 us
Input len: 23 	Time: 0.16 us
Input len: 24 	Time: 0.141 us
Input len: 25 	Time: 0.16 us
Input len: 26 	Time: 0.142 us
Input len: 27 	Time: 0.142 us
Input len: 28 	Time: 0.142 us
Input len: 29 	Time: 0.141 us
```

And a plot will appear:

![constant_time](media/O(1).png)

There is no correlation between input length and time, which suggests complexity is O(1).

For another example, check out ```examples/good_pairs.py```, where an O(n^2) algorithm is timed. Plot is below:

![quad_time](media/O(n^2).png)

