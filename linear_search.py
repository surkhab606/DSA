# LINEAR SEARCH : 0(n)^2
# Search through array one by one, comparing values. 


def linear_search(arr, target):
    for i in range(len(arr) - 1):
        if arr[i] == target:
            return i

target = 8
arr = [1,2,3,8,4]
print(linear_search(arr, target))