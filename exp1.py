# math = 50
# name = "siddharth"
# pi = 3.14
# result = True 
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))
# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result)) 
# id is ued for address of the variable in memory


# math = 50
# chem = 50
# phy = 50
# mar = 40
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(mar)) // here we can see that the address of math, chem and phy are same because they have same value but mar has different value so it has different address      

# print(10+20)
# print("10"+"20") # here we are concatenating the string 10 and 20 so it will give us 1020 as output
# val1 = input("Enter value of val1: ")
# val2 = input("Enter value of val2: ")
# print(val1+val2) # here we are concatenating the string val1 and val

# input function by default takes input as string so if we want to take input as integer we have to convert it using int() function
# val1 = int(input("Enter value of val1: "))
# val2 = int(input("Enter value of val2: "))
# print(val1+val2) //here we are adding the integer values of val1 and`` val2 so it will give us the sum of val1 and val2 as output

#  int() used to convert in integer
# print(int(3.14)) # here we are converting the float value 3.14 to integer so it will give us 3 as output
# # print(int(10+5J)) # here we are converting the complex value 10+5j to integer so it will give us 10 as output
# print(int(True)) # here we are converting the boolean value True to integer so it will give us 1 as output
# print(int(False)) # here we are converting the boolean value False to integer so it will give us 0 as output
# print(int("4")) # here we are converting the string value "4" to integer so it will give us 4 as output
# print(int("4.5")) # here we are trying to convert the string value "4.5" to integer but it will give us error because we cannot convert a float string to integer directly we have to convert it to float first and then to integer


# float() used to convert in float
# print(float(3)) # here we are converting the integer value 3 to float so it will give us 3.0 as output
# # print(float(10+5J)) # here we are converting the complex value 10 + 5j to float but it will give us error because we cannot convert a complex value to float directly we have to convert it to integer first and then to float
# print(float(True)) # here we are converting the boolean value True to float so it will give us 1.0 as output
# print(float(False)) # here we are converting the boolean value False to float so it will give us 0.0 as output
# print(float("4.5")) # here we are converting the string value "4.5" to float so it will give us 4.5 as output
# print(float("4")) # here we are converting the string value "4" to float so it will give us 4.0 as output

# cannot convert complex value to float directly we have to convert it to integer first and then to float
# we cannot convert string value to float directly if it is not a valid float string like "4.5" or "4" otherwise it will give us error
  
# complex() used to convert in complex

# print(complex(3)) # here we are converting the integer value 3 to complex so it will give us 3+0j as output
# print(complex(3.14)) # here we are converting the float value 3.14 to complex so it will give us 3.14+0j as output
# print(complex(True)) # here we are converting the boolean value True to complex so it will give us 1+0j as output
# print(complex(False)) # here we are converting the boolean value False to complex so it will give us 0+0j as output
# print(complex("4")) # here we are converting the string value "4" to complex
# print(complex("4.5")) # here we are converting the string value "4.5" to complex
# print(complex(5,-3)) # here we are converting the integer values 5 and -3 to complex so it will give us 5-3j as output  
# print(complex(True, False)) # here we are converting the boolean values True and False to complex so it will give us 1+0j as output
# print(complex(3, 4)) # here we are converting the integer values 3 and 4 to complex so it will give us 3+4j as output   


# bool() used to convert in boolean
# print(bool(0)) # here we are converting the integer value 0 to boolean so it will give us False as output
# print(bool(1)) # here we are converting the integer value 1 to boolean so it will give us True as output  
# print(bool(-1)) # here we are converting the integer value -1 to boolean so it will give us True as output because any non zero value is considered as True in boolean
# print(bool(0.0)) # here we are converting the float value 0.0 to boolean so it will give us False as output
# print(bool(0.1)) # here we are converting the float value 0.1   to boolean so it will give us True as output because any non zero value is considered as True in boolean
# print(bool("")) # here we are converting the empty string value "" to boolean so it will give us False as output
# print(bool(" ")) # here we are converting the string value " " to boolean so it will give us True as output because any non empty string is considered as True in boolean
# print(bool("False")) # here we are converting the string value "False" to boolean so it will give us True as output because any non empty string is considered as True in boolean
# print(bool("True")) # here we are converting the string value "True" to boolean so it will give us True as output because any non empty string is considered as True in boolean
# print(bool(None)) # here we are converting the None value to boolean so it will give us False as output because None is considered as False in boolean  
# print(bool(1+2j)) # here we are converting the complex value 1+2j to boolean so it will give us True as output because any non zero value is considered as True in boolean  
# print(bool("siddharth")) # here we are converting the string value "siddharth" to boolean so it will give us True as output because any non empty string is considered as True in boolean

# // in boolean any non zero value is considered as True and any zero value is considered as False

# val1=int(input("Enter value of val1: "))
# val2=int(input("Enter value of val2: "))
# print("Value of val1 =",val1,"and val2 =",val2,"before swapping")
# temp=val1
# val1=val2
# val2=temp
# print("Value of val1 =",val1,"and val2 =",val2,"after swapping")
  

# num1=int(input("Enter value of num1: "))
# num2=int(input("Enter value of num2: "))
# print("Value of num1 =",num1,"and num2 =",num2,"before swapping")
# # swapping with just 2 variables without using temp variable
# num1=num1+num2
# num2=num1-num2
# num1=num1-num2


# num1,num2=num2,num1 # here we are swapping the values of num1 and num2 using tuple unpacking
# print("Value of num1 =",num1,"and num2 =",num2,"after swapping")

# math =int(input("Enter value of math: "))
# chem =int(input("Enter value of chem: "))
# phy =int(input("Enter value of phy: "))
# total = math + chem + phy
# # percentage= (total/300)*100
# percentage= total/3
# print("Total marks =",total)    
# print("Percentage =",percentage)

# principal = int(input("Enter value of principal: "))
# rate = int(input("Enter value of rate: "))
# time = int(input("Enter value of time: "))
# simple_interest = (principal * rate * time) 
# print("Simple Interest =", simple_interest)

# principal = float(input("Enter value of principal: "))
# rate = float(input("Enter value of rate: "))
# time = float(input("Enter value of time: "))
# simple_interest = (principal * rate * time) 
# print("Simple Interest =", simple_interest)

# height=float(input("Enter value of height in feet: "))
# inches=height*12 
# cm=inches*2.54
# print("Height in inches =",inches)
# print("Height in cm =",cm)
# # write  a program to convert height in feet to inches and cm my height is 5.11 so i will enter 5.11 as input and it will give me the height in inches and cm as output value of inches will be 71.32 and value of cm will be 181.61
# height_input = input("Enter value of height in feet (e.g. 5.11 for 5ft 11in or 5.9167 for decimal feet): ")

# # Support both feet.inches style and decimal feet style
# if "." in height_input:
#     feet_part, frac_part = height_input.split(".", 1)
#     try:
#         feet = float(feet_part)
#         inches_fraction = float(frac_part)
#     except ValueError:
#         raise ValueError("Invalid input. Please use numeric values like 5.11 or 5.9")

#     # If the fractional part is less than 12, treat as feet.inches (e.g., 5.11 -> 5ft 11in).
#     # Otherwise treat as decimal feet (e.g., 5.9167).
#     if 0 <= inches_fraction < 12 and frac_part == str(int(inches_fraction)):
#         total_inches = feet * 12 + inches_fraction
#     else:
#         total_inches = (feet + inches_fraction / 100.0) * 12 if len(frac_part) <= 2 else float(height_input) * 12
# else:
#     total_inches = float(height_input) * 12

# cm = total_inches * 2.54
# print(f"Height in inches = {total_inches:.2f}")
# print(f"Height in cm = {cm:.2f}")
# # For 5.11 as feet.inches, this gives 71.00? Wait if feet=5, inches=11 -> 71.00, 180.34.
# # Correction: 5.11 means 5ft 11in. 5ft 11in -> 71.00 in -> 180.34 cm.


# reverse of a number
# num =123
# a=num%10
# num=num//10
# b=num%10
# num=num//10 
# c=num%10
# rev=a*100+b*10+c
# print("Reverse of the number is =",rev)


# num = 123456
# rev = 0
# while num > 0:  
#     a = num % 10
#     rev = rev * 10 + a
#     num = num // 10
# print("Reverse of the number is =", rev)

# num =123456
# a=num%10
# num=num//10
# b=num%10
# num=num//10
# c=num%10
# num=num//10     
# d=num%10
# num=num//10
# e=num%10
# num=num//10
# f=num%10
# rev=a*100000+b*10000+c*1000+d*100+e*10+f
# print("Reverse of the number is =",rev)



# a =20
# b =20
# print(a is b) # here we are checking if a and b are pointing to the same object in memory or not so it will give us True as output because both a and b are pointing to the same object in memory which is 20
# print(a is not b) # here we are checking if a and b are pointing to different objects in memory or not so it will give us False as output because both a and b are pointing to the same object in memory which is 20


# name= "siddharth"
# print('t' in name) # here we are checking if the character 't' is present in the string name or not so it will give us True as output because the character 't' is present in the string name which is "siddharth"
# print('z' in name) # here we are checking if the character 'z' is present in the string name or not so it will give us False as output because the character 'z' is not present in the string name which is "siddharth"
# print('s' not in name) # here we are checking if the character 's' is not present in the string name or not so it will give us False as output because the character 's' is present in the string name which is "siddharth"
# print('z' not in name) # here we are checking if the character 'z' is not present in the string name or not so it will give us True as output because the character 'z' is not present in the string name which is "siddharth"





# num=int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")
# if num < 0:
#     print("The number is negative")
# if num == 0:
#     print("The number is zero") 

# Simple if statement

# num1=int(input("Enter a number1:"))
# num2=int(input("Enter another number2: "))
# num3=int(input("Enter a third number3 :"))
# num4=int(input("Enter a fourth number4:"))
# num5=int(input("Enter a fifth number5: "))
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#     print("The greatest number is:", num1)
# if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#     print("The greatest number is:", num2)
# if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#     print("The greatest number is:", num3)
# if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#     print("The greatest number is:", num4)
# if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
#     print("The greatest number is:", num5)


# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == password:
#     print("Login successful!")  
# else:
#     print("Invalid username or password. Please try again.")


# If-Else with logical operators

# phy = int(input("Enter value of physics marks: "))
# chem = int(input("Enter value of chemistry marks: "))
# math = int(input("Enter value of mathematics marks: "))
# gender= input("Enter your gender (M/F): ")
# total= phy + chem + math
# percentage = total / 3
# print("Total marks =", total)
# print("Percentage =", percentage)
# if percentage >=60 and gender == 'M':
#     print("You are eligible for placement")
# else:
#     print("Eligible for data entry")


# a=int(input("Enter value of a: "))
# b=int(input("Enter value of b: "))
# c=int(input("Enter value of c: "))
# if a > b:
#     if a > c:
#         print("The greatest number is:", a)
#     else:
#         print("The greatest number is:", c)
# else:
#     if b > c:
#         print("The greatest number is:", b)
#     else:
#         print("The greatest number is:", c)



# day=input("Enter a day of the week: ")
# if day == "Monday" or day == "monday" or day == "Tuesday" or day == "tuesday" or day == "Wednesday" or day == "wednesday" or day == "Thursday" or day == "thursday" or day == "Friday" or day == "friday":
#     print("It's a working day")
# else:
#     print("It's a weekend")



# ord takes a character as input and returns its corresponding ASCII value as output it takes only one character as input and if we try to take more than one character as input it will give us error because it cannot convert more than one character to ASCII value
# ch=ord(input("Enter a value: ")) # here we are taking input from the user and converting it to its corresponding ASCII value using ord() function so that we can check if it is a string or a number or a special character
# if (ch >= 48 and ch <= 57): # here we are checking if the ASCII value is between 48 and 57 which corresponds to the digits 0 to 9
#     print("It's a digit")
# elif (ch >= 65 and ch <= 90): # here we are checking if the ASCII value is between 65 and 90 which corresponds to the uppercase letters A to Z
#     print("It's an uppercase letter")
# elif (ch >= 97 and ch <= 122): # here we are checking if the ASCII value is between 97 and 122 which corresponds to the lowercase letters a to z
#     print("It's a lowercase letter")
# else:
#     print("It's a special character")


# amt=int(input("Enter the amount for withdrawal: "))
# print("500 notes =", amt//500)    // here we are calculating the number of 500 notes required for the given amount by using floor division operator // which gives us the quotient without the remainder so it will give us the number of 500 notes required for the given amount as output    
# amt=amt%500       //  here we are calculating the remaining amount after giving the 500 notes by using modulus operator % which gives us the remainder after dividing the amount by 500 so it will give us the remaining amount after giving the 500 notes as output
# print("200 notes =", amt//200) 
# amt=amt%200
# print("100 notes =", amt//100)
# amt=amt%100
# print("50 notes =", amt//50)
# amt=amt%50
# print("20 notes =", amt//20)
# amt=amt%20
# print("10 notes =", amt//10)
# amt=amt%10
# print("5 coins =", amt//5)
# amt=amt%5
# print("2 coins =", amt//1)
# amt=amt%1
# print("1 coins =", amt//1)
  