import numpy as np

def FizzBuzz(start, finish):
    x = np.arange(start, finish + 1)
    out = np.array(x, dtype=object)

    m3 = (x % 3) == 0
    m5 = (x % 5) == 0

    out[m3] = "fizz"
    out[m5] = "buzz"
    out[m3 & m5] = "fizzbuzz"

    return out.tolist()
