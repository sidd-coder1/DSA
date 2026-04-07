# in list odd number should come after the even number
list=int(input("enter the size of the list"))
even=[]
odd=[]
for i in range(list):
    num=int(input("Enter the number"))
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers are:",even)
print("Odd numbers are:",odd)
print(even+odd)