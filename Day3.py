# Rearrange Positive and negative numbers arrange in alternate like 1,-2,
# arr=[-1,2,-3,4,5,-6]
# positive=[]
# negative=[] 
# for i in arr:
#     if i>0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print(positive)
# print(negative)
#  this output will print the positive and negative numbers in separate lists. You can further rearrange them in alternate order if needed.
# writ the code which arrange the given array in aiternate manner positive negative like 1,-2,3,-4,5,-6
# arr=[-1,2,-3,4,5,-6]
# positive=[]
# negative=[]
# for i in arr:
#     if i>0:
#         positive.append(i)
#     else:
#         negative.append(i)  
# result=[]
# for i in range(max(len(positive),len(negative))):
#     if i<len(positive):
#         result.append(positive[i])
#     if i<len(negative):
#         result.append(negative[i])
# print(result) # it will print the rearranged array in alternate manner positive negative like 1,-2,3,-4,5,-6

# Find the majority element in an array(element which appears more than n/2 times in the array)
# def find_majority_element(arr):
#     count={}
#     for i in arr:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     majority_element=None
#     for key,value in count.items():
#         if value>len(arr)//2:
#             majority_element=key
#             break
#     return majority_element
# print(find_majority_element([3,3,4,2,4,4,2,4,4])) # it will print the majority element in the array which is 4 in this case

# give me simple program to find the majority element in an array using for loop and if else statement without using any extra space
# def find_majority_element(arr):
#     majority_element=None
#     count=0
#     for i in arr:
#         if count==0:
#             majority_element=i
#             count=1
#         elif i==majority_element:
#             count+=1
#         else:
#             count-=1
#     return majority_element
# print(find_majority_element([3,3,4,2,4,4,2,4,4])) # it will print the majority element in the array which is 4 in this case



# ---------------------------------------= DIctionary =-----------------------------------
# dict repesented by key value pairs parenthesis is used to define a dictionary
# duplictae keys are not allowed in a dictionary but duplicate values are allowed in a dictionary
# it is mutable data type which means we can change the values of a dictionary
# unordered data type which means the order of the elements in a dictionary is not maintained

# mydict={
#     101:"siddharth",
#     102:"priyanshu",
#     "103":"mohini",
#     "104":"trivani",
#     101:"priyanshu", # it will overwrite the value of key 101 with "priyanshu" because duplicate keys are not allowed in a dictionary
#     104:"priyanshu" # it will overwrite the value of key 104 with "priyanshu" because duplicate keys are not allowed in a dictionary
# }
# print(mydict) # it will print the dictionary with the updated values for keys 101 and 104
# with the help of key we have to print the value of a dictionary

# a=mydict[102] # it will print the value of key 102 which is "priyanshu"
# print(a)

# mydict[102]="peter"
# print(mydict) # it will print the dictionary with the updated value for key 102 which is "peter"


# only print the keys of a dictionary
# for x in mydict:
#     print(x) # it will print the keys of the 
    

# for x in mydict.values():
#     print(x) # it will print the values of the dictionary

# for x in mydict:
#     print(mydict[x]) # it will print the values of the dictionary using the keys

# for x, y in mydict.items():
#     print(x, y) # it will print the key value pairs of the dictionary in the form of tuples

# mydict["mobile no"]=468987658
# print(mydict) # it will print the dictionary with the new key value pair "mobile no": 468987658


# MCQ 
# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a={'a':1,'b':2,'c':3}
# print(a['a','b'])  it will give an error because we are trying to access thenvalue of a key


# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# print(arr) # it will print the dictionary with the updated values for keys 1 and '1' which are 2 and 2 respectively

# sum=0
# for k in arr:
#     sum+=arr[k]

# print(sum) # it will print the sum of the values of the dictionary which is 4 in this case

# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict) # it will print the dictionary with the updated values for keys 1, '1' and 1.0 which are 4, 2 and 4.2 respectively because 1 and 1.0 are considered as the same key in a dictionary and their values are added together which gives us 2+4.2=6.2

# sum=0
# for k in my_dict:
#     sum+=my_dict[k]
# print(sum) # it will print the sum of the values of the dictionary which is 6 in this case because 1 and 1.0 are considered as the same key in a dictionary and their values are added together which gives us 2+4=6


# mydict={}
# mydict[(1,2,4)]=8
# mydict[(4,2,1)]=10
# mydict[(1,2)]=12
# print(mydict) # it will print the dictionary with the updated key value pairs (1,2,4): 8, (4,2,1): 10 and (1,2): 12 because tuples are immutable data type and they can be used as keys in a dictionary
# sum=0
# for k in mydict:
#     sum+=mydict[k]
# print(sum)  

# box={}
# jars={}
# crates={}
# box["biscuit"]=1
# box["chocolate"]=2
# jars["jam"]=4
# crates['box']=box
# crates['jars']=jars 

# print(len(crates[box])) # it will print the length of the dictionary which is 2 in this case because there are 2 key value pairs in the dictionary box

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_]) # it will print the keys of the dictionary in sorted order which is 'a', 'b' and 'c' in this case  

# rec={"name":"python","age":"30"}
# r=rec.copy()
# print(id(r)==id(rec)) # it will print the id of the copied dictionary r and the original dictionary rec which will be different because they are two different objects in memory
# print(r) # it will print the copied dictionary r which is {'name': 'python', 'age': '30'} in this case
# print(id(r)) # it will print the id of the copied dictionary r which is different from the id of the original dictionary rec
# print(id(rec)) # it will print the id of the original dictionary rec which is different from the id of the copied dictionary r

# rec={"name":"python","age":"30"}
# id1=id(rec)
# print(id1) # it will print the id of the original dictionary rec which is a unique identifier for the object in memory
# del rec
# print(id(rec))
# print(rec) # it will give an error because we have deleted the original dictionary rec and it is no longer available in memory
# rec={"name":"python","age":"30"}
# id2=id(rec)
# print(id2) # it will print the id of the new dictionary rec which is a unique identifier for the new object in memory and it will be different from the id of the original dictionary rec because we have deleted the original dictionary and created a new one with the same name but it is a different object in memory   
# print(id1==id2) # it will print False because the id of the original dictionary rec and the id of the new dictionary rec are different because they are two different objects in memory 

# find key with minimum value in a dictionary
# mydict={"x":20,"y":10,"z":30}
# min_key=None
# min_value=float('inf')
# for key,value in mydict.items():
#     if value<min_value:
#         min_value=value
#         min_key=key
# print(min_key) # it will print the key with the minimum value in the dictionary which is "y" in this case because it has the minimum value of 10 among all the key value pairs in the dictionary
# print(min_value) # it will print the minimum value in the dictionary which is 10 in this case because it is the minimum value among all the key value pairs in the dictionary


# mydict={
#     101:"siddharth",
#     "professional":"software developer",
#     "empid":1001,

# }
# mydict.pop(101) # it will remove the key value pair with key 101 from the dictionary and return the value "siddharth" in this case
# print(mydict) # it will print the dictionary with the key value pair with key 101 removed which is {'professional': 'software developer', 'empid': 1001} in this case

    # for i in range(1,4):
    #     for j in range(1,4):
    #        print(i, end=" ") # it will print the numbers from 1 to 3 in a matrix form with spaces in between
    #     print() # it will print a new line after each row of the matrix is printed

# print * pattern in the form of a matrix
# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ") # it will print the * pattern in the form of a matrix with spaces in between
#     print() # it will print a new line after each row of the matrix is printed

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ") # it will print the numbers from 1 to n in a right angled triangle with spaces in between
#     print() # it will print a new line after each row of the triangle is printed

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(64+i), end=" ") # it will print the letters from A to the nth letter in a right angled triangle with spaces in between
#     print() # it will print a new line after each row of the triangle is printed

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i): # n+2-i will give us the number of columns to be printed in each row of the triangle and it will decrease by 1 in each subsequent row which will give us the right angled triangle pattern
#         print("*", end=" ") # it will print the letters from A to the nth letter in a right angled triangle with spaces in between
#     print() # it will print a new line after each row of the triangle is printed

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j), end=" ") # it will print the letters from A to the nth letter in a right angled triangle with spaces in between and it will decrease by 1 in each subsequent row which will give us the right angled triangle pattern
#     print() # it will print a new line after each row of the triangle is printed

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     time.sleep(0.5) # it will add a delay of 0.5 seconds before printing each row of the triangle which will give us a better visual effect of the triangle being printed
#     for j in range(1,n+2-i):
#         time.sleep(1) # it will add a delay of 0.5 seconds before printing each character in the triangle which will give us a better visual effect of the triangle being printed
#         print(n+1-i, end=" ") # it will print the letters from A to the nth letter in a right angled triangle with spaces in between and it will decrease by 1 in each subsequent row which will give us the right angled triangle pattern
#     print() # it will print a new line after each row of the triangle is printed

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i), end=" ") # it will print the spaces before the numbers in each row of the triangle which will give us the right angled triangle pattern
#     for j in range(1,i+1):
#         time.sleep(1) # it will add a delay of 0.5 seconds before printing each character in the triangle which will give us a better visual effect of the triangle being printed
#         print("*", end=" ") # it will print the numbers from 1 to n in a right angled triangle with spaces in between
#     print() # it will print a new line after each row of the triangle is printed





# ---------------------------Function in python---------------------------

# def msg():   # function definition
#     print("hello world") # it will print "hello world" when the function is called
# msg() # function call
# msg() # function call

# def arithmetic():
#     a=int(input("Enter the value of a: "))
#     b=int(input("Enter the value of b: "))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div # it will return the values of add, sub, mul and div as a tuple when the function is called
# # print(arithmetic()) # it will call the arithmetic function and print the returned values of add, sub, mul and div as a tuple
# result=arithmetic() # it will call the arithmetic function and store the returned values of add, sub, mul and div as a tuple in the variable result
# print("Arithmetic operations:", result) # it will print the values of add, sub, mul and div as a tuple which is stored in the variable result

# How many types of arguments we can pass in a function in python
# 1. Positional arguments:      these are the arguments which are passed to the function in the same order as they are defined in the function definition
# 2. Keyword arguments:         these are the arguments which are passed to the function with the
#                               name of the parameter and the value of the argument in the form of key value pairs
# 3. Default arguments:         these are the arguments which are defined in the function definition with a default value and if the argument is not passed to the function then the default value will be used
# 4. Variable length arguments: these are the arguments which are defined in the function definition with an asterisk (*) before the parameter name and it can take any number of arguments as input and it will be stored as a tuple in the parameter 



# Positional arguments
# def login(x, y): # it is a function definition with two parameters username and password which are positional arguments because they are passed to the function in the same order as they are defined in the function definition
#      if username==password: 
#          print("Login successful!")
#      else:
#          print("Invalid username or password.")

# username=input("Enter your username: ")
# password=input("Enter your password: ")
# login(username, password) # it will call the login function but it will not do anything because the function body is empty and it has a pass statement which does nothing when the function is called

# Keyword arguments
# def  login(username, password): # it is a function definition with two parameters username and password which are keyword arguments because they are passed to the function with the name of the parameter and the value of the argument in the form of key value pairs
#      if username==password: 
#          print("Login successful!")
#      else:
#          print("Invalid username or password.")
# login(username="admin", password="admin") # it will call the login function with the keyword arguments username and password and it will print "Login successful!" because the value of username and password are the same which is "admin" in this case

# Default arguments
# def cityName(city="Delhi"): # it is a function definition with a parameter city which is a default argument because it is defined in the function definition with a default value "Delhi" and if the argument is not passed to the function then the default value will be used
#     print(city) # it will print the name of the city which is passed as an argument to the function

# cityName("Mumbai") # it will call the cityName function with the argument "Mumbai" and it will print "Mumbai" because it is the value of the argument passed to the function
# cityName() # it will give an error because the cityName function is defined with a parameter city which is a required parameter and it does not have a default value and we are trying to call the function without passing any argument which is required for the function to work properly

# variable length arguments
# def nameOfCitys(*city): # it is a function definition with a parameter city which is a variable length argument because it is defined in the function definition with an asterisk (*) before the parameter name and it can take any number of arguments as input and it will be stored as a tuple in the parameter city
#     print("City Names = ",city) # it will print the names of the cities which are passed as arguments to
    
# nameOfCitys("Delhi", "Mumbai", "Bangalore","Goa") # it will call the nameOfCitys function with the variable length arguments "Delhi", "Mumbai" and "Bangalore" and it will print the names of the cities which are passed as arguments to the function

# write a program for menu driven code
# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Result = ",a+b)
#         break
#     elif choice == 2:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Result = ",a-b)
#         break
#     elif choice == 3:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Result = ",a*b)
#         break
#     elif choice == 4:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         print("Result = ",a/b)
#         break
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice!")

import sys
# def add():  
#     val1=int(input("Enter first number: "))
#     val2=int(input("Enter second number: "))
#     print("Result = ",val1+val2)

# def sub():
#     val1=int(input("Enter first number: "))
#     val2=int(input("Enter second number: "))
#     print("Result = ",val1-val2)

# def mul():
#     val1=int(input("Enter first number: "))
#     val2=int(input("Enter second number: "))
#     print("Result = ",val1*val2)

# def div():
#     val1=int(input("Enter first number: "))
#     val2=int(input("Enter second number: "))
#     print("Result = ",val1/val2)

# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit() # it will exit the program when the user chooses to exit by entering 5 as their choice
#     else:
#         print("Invalid choice!")     



# rstrip() method is used to remove any trailing whitespace from the input string and it will compare the input string with "python" and if it matches then it will print the name of the programming language
# lstrip() method is used to remove any leading whitespace from the input string and it will compare the input string with "python" and if it matches then it will print the name of the programming language
# strip() method is used to remove any leading and trailing whitespace from the input string and it will compare the input string with "python" and if it matches then it will print the name of the programming language
# programming=input("Enter your favourite programming language: ")
# p_name=programming.rstrip()
# if p_name=="python":
#     print(p_name) # it will print the name of the programming language which is "python" in this case because we have used the rstrip() method to remove any trailing whitespace from the input string and it will compare the input string with "python" and if it matches then it will print the name of the programming language
# elif p_name=="java":
#     print(p_name) # it will print the name of the programming language which is "java" in this case because we have used the rstrip() method to remove any trailing whitespace from the input string and it will compare the input string with "java" and if it matches then it will print the name of the programming language
# elif p_name=="c++":
#     print(p_name) # it will print the name of the programming language which is "c++" in this case because we have used the rstrip() method to remove any trailing whitespace from the input string and it will compare the input string with "c++" and if it matches then it will print the name of the programming language
# else:
#     print("Invalid input!") # it will print "Invalid input!" if the input string does not match with any of the programming languages which are "python", "java" and "c++" in this case 


