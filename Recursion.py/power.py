


# why we use recursion , if its time complexity is more and space complexity is more than iteration?

# --> We use reccursion especially in the cases we know that a problem can be broken down into smaller subproblems of the same type.
#  It can make code more elegant and easier to understand, especially for problems that have a natural recursive structure, such as tree traversal, graph traversal, and divide-and-conquer algorithms.
#  In some cases, recursion can lead to cleaner and more intuitive code compared to iterative solutions. 
# However, it's important to be mindful of the potential for stack overflow with deep recursion and to consider iterative solutions when performance is a concern.


# def PowerOfTwo(n):
#     if n==0:
#         return 1
#     else:
#         return 2*PowerOfTwo(n-1)
# number=int(input("Enter a number to calculate its power of two: "))
# result=PowerOfTwo(number)   
# print(f"2 raised to the power of {number} is {result}.")


# using loop
# def powerOfTwo(n):
#     i=0
#     power=1
#     while i<n:
#         power*=2
#         i+=1
#     return power
# number=int(input("Enter a number to calculate its power of two: "))
# result=powerOfTwo(number)
# print(f"2 raised to the power of {number} is {result}.")

def Power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * Power(base, exponent - 1)
print(Power(2,0))
print(Power(2,4))
print(Power(2,6))
print(Power(6,2))
print(Power(3,5))


