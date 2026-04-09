# find biggest number in array
def biggest(arr): # time complexity of this function is O(n) because we are iterating through the array once to find the biggest number
    biggestNumber=arr[0] # we are assuming that the first element of the array is the biggest number
    # time complexity of this line is O(1) because we are just assigning the value of the first element of the array to the variable biggestNumber
    for i in arr: # we are iterating through the array to find the biggest number
                  #time complexity of this line is O(n) because we are iterating through the array once to find the biggest number
        if i>biggestNumber: # if the current element is greater than the biggest number, then we are updating the biggest number
                            # time complexity of this line is O(1) because we are just comparing the current element with the biggest number and updating the biggest number if the current element is greater than the biggest number
            biggestNumber=i   # time complexity of this line is O(1) because we are just updating the value of the biggest number with the current element if the current element is greater than the biggest number
    return biggestNumber  #TIME COMPLEXITY OF THIS LINE IS O(1) BECAUSE WE ARE JUST RETURNING THE VALUE OF THE BIGGEST NUMBER
arr=[1,2,3,4,5]  #TIME COMPLEXITY OF THIS LINE IS O(1) BECAUSE WE ARE JUST INITIALIZING THE ARRAY WITH SOME VALUES
print("The biggest number in the array is:",biggest(arr)) #TIME COMPLEXITY OF THIS LINE IS O(1) BECAUSE WE are just printing the value of the biggest number in the array

# the final time complexity of this code is O(n) 
# because we are iterating through the array once to find the biggest number and all other operations are O(1)





# Rule 1 :Any assignment  statements and if statements are executed once regardless of the size 
# of the problem . These statements have a constant time complexity of O(1) .


# Rule 2 : a simple loop "for" loop from 0 to n(with no internal loops) has a linear time complexity of O(n) because it iterates through the loop n times.
# Rule 3 : a nested loop "for" loop inside another "for" loop has a quadratic time complexity of O(n^2) because it iterates through the outer loop n times and for each iteration of the outer loop, 
# it iterates through the inner loop n times, resulting in n*n = n^2 iterations.

# Rule 4: A loop, in which the controlling parameter is divided by a two at each step has a logarithmic time complexity of O(log n) because it reduces the number of iterations by half at each step, resulting in log n iterations.


