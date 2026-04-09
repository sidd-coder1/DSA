def linear_search(arr, target): # time complexity of this function is O(n) because we are iterating through the array once to find the target element
    for i in range(len(arr)): # time complexity of this line is O(n) because we are iterating through the array once to find the target element
        if arr[i] == target: # if the current element is equal to the target element, then we are returning the index of the target element
            return i # time complexity of this line is O(1) because we are just returning the index of the target element
    return -1 # time complexity of this line is O(1) because we are just returning -1 if the target element is not found in the array

arr=[1,2,3,4,5] # time complexity of this line is O(1) because we are just initializing the array with some values
target=55 # time complexity of this line is O(1) because we are just initializing the target element with some value
result=linear_search(arr, target) # time complexity of this line is O(n) because we are calling the linear_search function which has a time complexity of O(n)
if result != -1:           # if the target element is found in the array, then we are printing the index of the target element
    print("Element found at index:", result)    # time complexity of this line is O(1) because we are just printing the index of the target element
else: 
    print("Element not found in the array")       # time complexity of this line is O(1) because we are just printing a message saying that the target element is not found in the array

# the final time complexity of this code is O(n) because we are iterating through the array once to find the target element and all other operations are O(1)


