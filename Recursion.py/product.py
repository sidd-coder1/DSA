def productOfArray(arr):
    if len(arr)==0:
        return 1
    return arr[0]*productOfArray(arr[1:])
arr=list(map(int,input("Enter a list of numbers separated by spaces: ").split()))
print(arr)
print("The product of the array is:", end=" ")
print(productOfArray(arr))  # Output: 6