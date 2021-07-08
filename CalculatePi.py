# Approximate pi using random number generator

import random
import time
import math


def calculate_pi(n):
    num_inside = 0
    for i in range(n):
        if random.uniform(0,1)**2 + random.uniform(0,1)**2 <= 1:
            num_inside += 1
    return num_inside/n * 4


n = 1000
trials = 100

pi = math.pi
avg_error = 0


for i in range(trials):
    before = time.monotonic()
    experimental = calculate_pi(n)
    error = pi - experimental
    avg_error += error
    print(str(calculate_pi(n)) + " with error " + str(error))
    after = time.monotonic()
    # print(str(after - before) + " seconds")


avg_error /= trials
print(avg_error)
