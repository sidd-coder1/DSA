# mylist=["apple","banana","cherry","orange",24,"kiwi","melon","mango",23,"grape","apple"]
# print(mylist)
# mylist.append("watermelon") # it will add "watermelon" to the end of the list
# print(mylist)
# mylist.insert(2,"strawberry") # it will add "strawberry" at index 2 of the list
# print(mylist)   
# print(mylist[0]) # it will print the first element of the list
# print(mylist[1:5]) # it will print the elements from index 1 to index 4
# print(mylist[-1]) # it will print the last element of the list          
# print(mylist[1:8:2]) # it will print every second element from index 1 to index 7
# print(mylist[::2]) # it will print every second element of the list
# print(mylist[1::]) # it will print the elements from index 1 to the end of the list
# print(mylist[:5]) # it will print the first 5 elements of the list  
# print(mylist[:]) # it will print the whole list
# print(mylist.count("apple")) # it will print the number of occurrences of "apple"
# print(mylist.index("kiwi")) # it will print the index of the first occurrence of "kiwi"
# mylist.append(1)
# print(mylist)
# mylist.insert(3,"rajdhani")
# print(mylist)

# mylist[2]="strawberry" # it will change the element at index 2 to "strawberry"
# print(mylist)

# if "banana" in mylist:
#     print("banana is present in the list") # it will print "banana is present in the list" if "banana" is present in the list
# else:
#     print("banana is not present in the list") # it will print "banana is not present in the list" if "banana" is not present in the list

# representation of stack ,queue, tree , using list

# mylist.append("Junglee") # it will add "Junglee" to the end of the list
# print(mylist)

# mylist.insert(2,"Rowdy") # it will add "Rowdy" at index 2 of the list
# print(mylist)

# mylist.remove("cherry") # it will remove the first occurrence of "cherry" from the list
# print(mylist)

# newList=mylist.copy() # it will create a copy of the list
# print("newList",newList)


# mylist=[['siddharth','singh'],[85.56],[440022,"yyy"]]
# print(mylist) # it will print the list of lists
# print(mylist[0]) # it will print the first list in the list of lists
# print(mylist[1]) # it will print the second list in the list of lists   
# print(mylist[0][1]) # it will print the second element of the first list in the list of lists
# print(mylist[2][0]) # it will print the first element of the third list in the list of lists
# print(mylist[2][1]) # it will print the second element of the third list in the list of lists
# print(mylist[2][0:2]) # it will print the first two elements of the third list in the list of lists

# list1=["siddharth","singh"]
# print(list1*2) # it will print the list1 twice


# list2=[50,70,90]
# print(list2)
# # print(list2+list1) # it will print the concatenation of list1 and list2
# # del list2
# # print(list2) # it will give an error because list2 has been deleted
# del list2[0] # it will give an error because list2 has been deleted
# print(list2) 
# del list2[1] # it will give an error because list2 has been deleted
# print(list2)    

# list=["siddharth","singh",85.56,440022,"yyy"]
# print(list) # it will print the original list
# list.clear() # it will remove all the elements from the list
# print(list) # it will print an empty list

# name="siddharth singh"
# print(name) # it will print the original string
# myname=list(name) # it will convert the string into a list of characters
# print(myname) # it will print the list of characters

# list=["siddharth","singh",85.56,440022,"yyy"]
# list.reverse() # it will reverse the order of the elements in the list
# print(list) # it will print the reversed list

# list=["mango","apple","banana","cherry","grape"]
# list.sort() # it will sort the elements of the list in ascending order
# print(list) # it will print the sorted list
# list.sort(reverse=True) # it will sort the elements of the list in descending order
# print(list) # it will print the sorted list in descending order

# default sorting order is numbersid ascending order and strings in alphabetical order
# list shouild contain elements of the same data type for sorting to work properly



# Alising a list
# list=["siddharth","singh",85.56,440022,"yyy"]
# mylist=list # it will create a new reference to the same list
# print(id(list)) # it will print the ID of the original list
# print(id(mylist)) # it will print the ID of the aliased list
# list[0]="rajdhani" # it will change the first element of the original list to "rajdhani"
# print(list) # it will print the modified original list
# print(mylist) # it will print the modified aliased list because both list and mylist refer to the same list

# MCQs

    # arr=[[1,2,3,4],
    #      [4,5,6,7],
    #      [8,9,10,11],
    #     [12,13,14,15]
    #      ]
    # for i in range(0,4):
    #     print(arr[i].pop()) # it will print the last element of each sublist in the 2D list and remove it from the original list
# print(arr) # it will print the modified 2D list after popping the last element from


# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i] # it will shift the elements of the list to the left by one position
# for i in range(0,6):
#     print(arr[i],end ="")   # it will print the modified list after shifting the elements to the left by one position


# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a) # it will replace every second element of the list with the values 10,20,30,40,50,60


# a=[1,2,3,4,5,6,7,8,9]
# print(a[3:0:-1])



# Tuple is a collection data type that is ordered and immutable. It is defined by enclosing the elements in parentheses () and separating them with commas.
# Duplicates are allowed in a tuple. It can contain elements of different data types. It is indexed and supports slicing. It is used to store a collection of items that should not be changed after creation.
# tuple by nature is growable.
# how can we decide to use a list or a tuple in our program?
# tuple is used when we want to store a collection of items that should not be changed after creation, while list is used when we want to store a collection of items that can be changed after creation. Tuple is more memory efficient than list because it is immutable and does not require extra memory for storing the elements. Tuple can be used as keys in a dictionary because it is immutable, while list cannot be used as keys in a dictionary because it is mutable.

# mytuple=("mango","apple","banana","cherry","grape",23,3.15,15,77,"sandip")
# print(mytuple) # it will print the original tuple
# print(type(mytuple)) # it will print the type of the tuple

# mytuple[2]="strawberry" # it will give an error because tuple is immutable and does not support item assignment
# print(mytuple) # it will not print anything because the previous line will give an error

# init_tuple=() # there is no element in the tuple it will print len as 0
# print(init_tuple.__len__()) # it will print the length of the empty tuple which is 0

# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(id(init_tuple_a)) # it will print the ID of init_tuple_a
# print(id(init_tuple_b)) # it will print the ID of init_tuple_b
# print(init_tuple_a==init_tuple_b) # it will print True because both init_tuple_a and init_tuple_b have the same elements in the same order
# this program is  comparing the memory addresses of two tuples and checking if they are equal. The output will show that both tuples have the same elements in the same order, but they are stored at different memory addresses because they are created as separate objects in memory. Therefore, the output will be something like:

# init_tuple_a='1','2'   //parenthesis are optional in tuple creation
# init_tuple_b=('3','4')
# print(init_tuple_a+init_tuple_b) # it will print the elements of init_tuple_a

# init_tuple=('Python')*3
# print(type(init_tuple)) # it will print the string "Python" repeated 3 times, which is "PythonPythonPython" 

# # init_tuple=('Python',)*3 # it will print the tuple ('Python', 'Python', 'Python') which is a tuple containing the string "Python" repeated 3 times as separate elements in the tuple
# print(type(init_tuple))

# init_tuple=(1,)*3
# init_tuple[0]=2 # it will give an error because tuple is immutable and does not support item assignment
# print(init_tuple) # it will not print anything because the previous line will give an error

# init_tuple=((1,2),)*7
# print(init_tuple) # it will print the tuple containing the tuple (1,2) repeated 7 times as separate elements in the outer tuple
# print(len(init_tuple[3:8]))


# names=[4,2,5,6,8,2]
# for i in names:
#     print(i) # it will print each element of the list "names" in a new line



# move the zeroes to the end of the list

# A=[4,0,2,5,0,1]
# for i in A:
#     if i==0:
#         A.remove(i) # it will remove the first occurrence of 0 from the list
#         A.append(i) # it will add 0 to the end of the list
# print(A) # it will print the modified list with zeroes at the end

# remove duplicates from the list and print only unique elements
# A=[1,2,2,3,4,4,5]
# for i in A:
#     if A.count(i)>1:
#         A.remove(i) # it will remove the first occurrence of the duplicate element from the list    
# print(A) # it will print the modified list with only unique elements


# find  out the common elements between three lists and print them in a new list
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i) # it will print the common elements between the three lists

#  write a program to calculate and return the sum of distances between the adjacent numbers in array of positive integers
# A=[10,11,7,12,14]
# sum=0
# length=len(A)
# print(length)
# for i in range(len(A)-1):
#     sum+=abs(A[i]-A[i+1]) # it will calculate the absolute difference between adjacent numbers and add it to the sum
# print(sum) # it will print the sum of distances between the adjacent numbers in the array

# n=int(input("Enter the size of array: "))
# arr=[]
# for i in range(n):
#     num=int(input("Enter the value of array: "))
#     arr.append(num) # it will add the input number to the array 
# print(arr) # it will print the original array
# sum=0
# for i in range(len(arr)-1):
#     sum+=abs(arr[i]-arr[i+1]) # it will calculate the absolute difference between adjacent numbers and add it to the sum
# print(sum) # it will print the sum of distances between the adjacent numbers in the array5


# for i in range(1,5):
#     if i==3:
#         break
#     print(i) # it will print the numbers from 1 to 4, but it will stop printing when it reaches 3 because of the break statement


# for i in range(1,6):
#      if i==3:
#         continue
#      print(i," ") # it will print the numbers from 1 to 4, but it will skip printing 3 because of the continue statement
#       # it will print the numbers from 5 to 1 in reverse order

# for i,j in zip(range(1,6),range(5,0,-1)):
#     print(i,"   ",j) # it will print the numbers from 1 to 5 and 6 to 10 in pairs using the zip function



# write a program to move * from given value and add the * in the start of the string
# Value="prashant*is*a*good*programmer"
# newValue=""
# val=''
# for i in Value:
#      if i!="*":
#          newValue+=i # it will add the character to the newValue string if it is not "*" 
#      else:
#          val+=i
# print(newValue) # it will print the modified string with all "*" moved to the start of the string
# print(val+newValue) # it will print the modified string with all "*" moved to the start of the string followed by the newValue string

# BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(id(x))
# print(id(y))
# print(id(z))
# print(x==y)
# print(x==z)
# print(x!=z)

# a = "listen"
# b = "silent"

# # Convert strings to list and sort
# a_sorted = sorted(a)
# b_sorted = sorted(b)

# print(a_sorted)
# print(b_sorted)

# if a_sorted == b_sorted:
#     print("Anagram")
# else:
#     print("Not an anagram")


# str='This is a statement'
# count=1
# for i in str:
#     if i ==' ':
#         count+=1
# print(count)



