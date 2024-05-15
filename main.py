import math

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from numba import njit
import random

class Counter:
    counter = 0

#@njit
def quicksort(nums, counter):
    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        pivot = nums[0]
        for x in nums:
            if x < pivot:
                less.append(x)
                counter.counter += 1
            elif x == pivot:
                equal.append(x)
                counter.counter += 1
            elif x > pivot:
                greater.append(x)
                counter.counter+=1
        # Don't forget to return something!
        return quicksort(less, counter) + equal + quicksort(greater, counter)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return nums

#@njit
def count_sort(i):
    MaxInt = 100000
    counter = Counter()
    nums = [random.randint(0, 1000) for j in range(i)]
    quicksort(nums, counter)
    return counter.counter

graphNode = list()
nlogn = list()
for i in tqdm(range(1, 1000)):
    nlogn.append(i*math.log2(i))
    graphNode.append(count_sort(i))

plt.plot(graphNode)
plt.plot(nlogn)
plt.show()