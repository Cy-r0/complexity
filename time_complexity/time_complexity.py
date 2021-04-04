from timeit import default_timer as timer

import matplotlib.pyplot as plt


def measure_time(func, repeat=1000):
    """
    Decorator that repeatedly executes a function
    and records lowest time.
    """

    def wrapper(*args, **kwargs):
        min_time = 1000

        for _ in range(repeat):
            start = timer()
            result = func(*args, **kwargs)
            curr_time = timer() - start
            if curr_time < min_time:
                min_time = curr_time

        return [min_time, result]
        
    return wrapper


def plot_complexity(func, inputs, repeat=1000):
    """
    Time a function for different input lengths 
    (input provided with a generator)
    and plot input length vs time.
    Args:
        func (callable): function to be timed.
        inputs (iterable): list or generator with input args for all input lengths.
        repeat (int): how many times to measure timing for each input length.
    """

    print(f"Plot complexity. Repeat: {repeat}")

    func = measure_time(func, repeat)

    lengths = []
    times = []

    print("Iterating over input lengths...")

    for args, input_len in inputs: 
        time, _ = func(*args)
        lengths.append(input_len)

        time *= 1e6 # Convert from s to us
        times.append(time)
        print(f"Input len: {input_len} \tTime: {time:.5} us")
    
    plt.plot(lengths, times, linestyle="-", marker="o")
    plt.xlabel("input length")
    plt.ylabel("time (us)")
    plt.xticks(lengths)
    plt.grid()
    plt.show()

