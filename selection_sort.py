# SELECTION SORT ALGO.: O(N)^2

# 1. Go through the array to find the lowest value.
# 2. Move the lowest value to the front of the unsorted part of the array.
# 3. Go through the array again as many times as there are values in the array.
# source: w3schools // https://www.w3schools.com/dsa/dsa_algo_selectionsort.php

def selection_sort(arr):

    # - 1 because of 0-based indexing. our outer loop moves us forward in the array step by step
    for i in range(len(arr) - 1):

        # the index of the smallest element. we will check if it truly is i, in the lines ahead
        smallest_index = i

        # because the value at i will be the smallest value in the array so far, we only want to sort the i + 1 part of the array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]


    return arr

arrayy = [5, 1, 2, 4, 9, 3]
print(selection_sort(arrayy))