# slicing 
# name ="Siddharth Singh"
# print(name[0:5]) # it will print the first 5 characters of the string
# print(name[6:13]) # it will print the characters from index 6 to index 12
# print(name[2])
# print(name[-1]) # it will print the last character of the string
# print(name[-2]) # it will print the second last character of the string
# print(name[0:]) # it will print the whole string
# print(name[:]) # it will also print the whole string    
# print(name[ :5]) # it will print the first 5 characters of the string
# print(name[5:]) # it will print the characters from index 5 to the end of the string
# print(name[::2]) # it will print every second character of the string   
# print(name[1:4:2]) # it will print every second character from index 1 to index 3
# print(name[::-1]) # it will print the string in reverse order   


# String define functions

# s="Python is a High level programming language"
# print(s.upper()) # it will print the string in upper case
# print(s.lower()) # it will print the string in lower case
# print(s.capitalize()) # it will print the string with first character in upper case
# print(s.title()) # it will print the string with first character of each word in upper case
# print(s.swapcase()) # it will print the string with upper case characters converted to lower case and vice versa
# print(s.count("o")) # it will print the number of occurrences of the character "o" in the string
# print(s.find("o")) # it will print the index of the first occurrence of the character "o" in the string
# print(s.rfind("o")) # it will print the index of the last occurrence of the character "o" in the string
# print(s.index("o")) # it will print the index of the first occurrence of the character "o" in the string
# print(s.rindex("o")) # it will print the index of the last occurrence of the character "o" in the string

# .format() function

# print=("Subject Marks")
# phy=50
# chem=90
# math=80
# print("physics{} chemistry{} mathematics{}".format(phy,chem,math)) # it will print the string with the values of phy, chem and math in the respective places
# print("physics{0} chemistry{1} mathematics{2}".format(phy,chem,math)) # it will print the string with the values of phy, chem and math in the respective places
# print("physics{x} chemistry{y} mathematics{z}".format(x=phy,y=chem,z=math)) # it will print the string with the values of phy, chem and math in the respective places   
# total=phy+chem+math
# print(f"Total marks: {total}") # it will print the total marks obtained in physics, chemistry and mathematics
# print("Roll Number=","46",zfill(4)) # it will print the roll number with leading zeros to make it 4 digits long




# Loops
# for loop

# for i in range(5):
#     print(i) # it will print the numbers from 0 to 4
# for i in range(1, 6):
#     print(i) # it will print the numbers from 1 to 5

# for i in range(1,11,2):
#     print(i) # it will print the odd numbers from 1 to 10
# for i in range(1,11):
#         print(i*2) # it will print the even numbers from 2's multiples from 1 to 10
# for i in range(1,11):
#           print("{:>3},{:>3},{:>3},{:>3},{:>3},{:>3},{:>3},{:>3},{:>3},{:>3}".format(i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10)) # it will print the even numbers from 2's multiples from 1 to 10 in a formatted way 
         
# print()
# for i in range(1,11):
#  print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20) # it will print the even numbers from 4's multiples from 1 to 10



# name ="racecar"
# for i in name:
#     print(i) # it will print each character of the string "racecar" in a new line

# write a program to remove dupliacates and print only unique characters from a string using for loop

# str="Hi Everyone Welcome to Python programming"
# unique=""
# for i in str:
#     if i not in unique:
#         unique+=i
# print(str)        
# print(unique)       


# for i in range(5,0,-1):
#     print(i) # it will print the numbers from 5 to 1 in reverse order
# for i in range(10,0,-2):
#     print(i) # it will print the even numbers from 10 to 2 in reverse order

# name="mumbai"
# rev=""
# for i in name[-1::-1]:
#     rev+=i
# print(rev)  # it will print the characters of the string "mumbai" in reverse order

# name="Hello"
# n=len(name)
# print(n)
# rev=""
# for i in range(n-1,-1,-1):
#     rev+=name[i]

# print(rev) # it will print the characters of the string "Hello" in reverse order


# checkk if it is palindrome or not

# name ="nitin"
# rev=""
# n=len(name)
# print(name)
# for i in range(n-1,-1,-1):
#     rev+=name[i]
# print(rev) # it will print the characters of the string "siddharth" in reverse order
# if name==rev:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")






