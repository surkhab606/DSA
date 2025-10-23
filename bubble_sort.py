# BUBBLE SORT. ALGO: O(N)^2

# 1. Go through the array, one value at a time.
# 2. For each value, compare the value with the next value.
# 3. If the value is higher than the next one, swap the values so that the highest value comes last.
# 4. Go through the array as many times as there are values in the array.
# source: w3schools // https://www.w3schools.com/dsa/dsa_algo_bubblesort.php

def bubble_sort(arr):

    # -1 because array indices start at 0. 
    for i in range(len(arr) - 1):

        # we only need to sort the inner part of the array because at the end of every iteration, the largest value
        # will be at the end. therefore, we can ignore the end values (the largest) and shorten the number of values
        # we go over each iteration.
        for j in range(len(arr) - i - 1):
            
            # if the value we're at currently is larger than the one next to it, we need to swap them.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)

arrayy = [5, 1, 2, 4, 9, 3]
print(bubble_sort(arrayy))