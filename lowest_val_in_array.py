# ALGO. FOR FINDING THE LOWEST VALUE IN AN ARRAY

def lowest_val(arr):
    lowest = arr[0]
    for i in arr: 
        if i < lowest:
            lowest = i
    
    return lowest