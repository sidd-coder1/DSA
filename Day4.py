# print('siddharthsingh8382'.isalnum()) # it will check if the string is alphanumeric or not and return True or False
# print('siddharthsingh8382'.isalpha()) # it will check if the string is alphabetic or not and return True or False
# print('777f'.isdigit()) # it will check if the string is numeric or not and return True or False
# print('SIDDHARTH'.isupper()) # it will check if the string is in uppercase or not and return True or False
# print('sdbsbd'.islower()) # it will check if the string is in lowercase or not and return True or False
# print(' '.isspace()) # it will check if the string is a whitespace or not and return True or False
# print('siddharthsingh8382'.startswith('s')) # it will check if the string starts with 's' or not and return True or False
# print('siddharthsingh8382'.endswith('2')) # it will check if the string ends with 'gh' or not and return True or False
# print('My name is Siddharth'.istitle()) # it will check if the string is in title case or not and return True or False

# print('siddharth'.find("M")) # it will return the index of the first occurrence of "M" in the string and if it is not found then it will return -1
# print('siddharth'.index("r")) # it will return the index of the first occurrence of "r" in the string and if it is not found then it will raise a ValueError
# print('siddharth'.count("d"))
# print('siddharth'.replace("s", "S"))    

# check if a key exist in a dictionary or not
# my_dict = {"name": "Siddharth", "age": 22, "city": "Delhi"}
# key=input("Enter a key to check: ")
# if key in my_dict:
#     print("Key exists in the dictionary")
# else:
#     print("Key does not exist in the dictionary")



# list=[1, 2, 2,3,4,3,5]
# # write a function to count the frequency of elements in the list using a dictionary
# def count_frequency(list):
#     frequency={}
#     for element in list:
#         if element in frequency:
#             frequency[element]+=1
#         else:
#             frequency[element]=1
#     return frequency
# print(count_frequency(list))




#----------------------------- Exception handling------------------------------
# Division by zero error handling using try-except block

# n1=int(input("Enter 1st number: "))
# n2=int(input("Enter 2nd number: "))
# try:
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except :
#     print("Error: Division by zero is not allowed")

# print("To be continued...")

# try:
#     n1=int(input("Enter 1st number: "))
#     n2=int(input("Enter 2nd number: "))
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid number.")
# print("To be continued...")

# we can also combine the except blocks for multiple exceptions by giving the exception types as a tuple in a single except block. This way we can handle multiple exceptions in a single block of code.
# try:
#     n1=int(input("Enter 1st number: "))
#     n2=int(input("Enter 2nd number: "))
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except (ZeroDivisionError, ValueError) as message:
#      print("Error: ", message) 
# print("To be continued...")





# try:
#     n1=int(input("Enter 1st number: "))
#     n2=int(input("Enter 2nd number: "))
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except (ZeroDivisionError, ValueError) as message:
#     print("Error: ", message) 
# except:                     #default except must always written after all the specific except blocks because it will catch all the exceptions that are not caught by the specific except blocks and if we write it before the specific except blocks then it will catch all the exceptions and the specific except blocks will never be executed.
#     print("An unexpected error occurred.")
# print("To be continued...")


# try:
#     n1=int(input("Enter 1st number: "))
#     n2=int(input("Enter 2nd number: "))
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except (ZeroDivisionError, ValueError) as message:
#     print("Error: ", message) 
# except:
#     print("An unexpected error occurred.")
# else:
#     print("The division was successful.")

# try:
#     n1=int(input("Enter 1st number: "))
#     n2=int(input("Enter 2nd number: "))
#     print("The division of the two numbers is: ", n1/n2) # this line will raise a ZeroDivisionError if n2 is 0
# except (ZeroDivisionError, ValueError) as message:
#     print("Error: ", message) 
# except:
#     print("An unexpected error occurred.")
# else:
#     print("The division was successful.")
# finally:
#     print("This block will always be executed regardless of whether an exception occurred or not. It is used to perform cleanup actions or to release resources that were acquired in the try block.")


# neted try-except blocks
# try:
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     try:
#         result=num1/num2
#         print("The division of the two numbers is: ", result) # this line will raise a ZeroDivisionError if num2 is 0
#     except ZeroDivisionError as message:
#         print("Error: ", message)
#     finally:
#         print("yahooo")
# except ValueError as message:
#     print("Error: ", message)
# finally:
#     print("Hurrahh")

# try:
#     num1=int(input("Enter 1st number: "))
#     num2=int(input("Enter 2nd number: "))
#     try:
#         result=num1/num2
#         print("The division of the two numbers is: ", result) # this line will raise a ZeroDivisionError if num2 is 0
#     except ZeroDivisionError as message:
#         print("Error: ", message)
# except ValueError as message:
#     print("Error: ", message)
# else:
#     print("The division was successful.")
# finally:
#     print("This block will always be executed regardless of whether an exception occurred or not. It is used to perform cleanup actions or to release resources that were acquired in the try block.")


#  write a program to find the security key which is the count of the repeating digits in  the data
# data=(input("Enter a number: "))
# frequency={}
# for digit in data:
#     if digit in frequency:
#         frequency[digit]+=1
#     else:
#         frequency[digit]=1
# security_key=0
# for digit, count in frequency.items():
#     if count > 1:
#         security_key+=count - 1 # we are subtracting 1 from the count because we are only interested in the repeating digits and not the unique digits
# print("The security key is: ", security_key)



# list=[7,3,9,2,8]
# list.sort() # it will sort the list in ascending order
# print(list)
# print(list[-2]) 
# print(list[3]) # it will print the second largest element of the list because the list is sorted in ascending order


# i=2
# while i<=20:
#     print(i)
#     i+=2

# username=""
# password=""
# while username!="admin" or password!="password":
#     username=(input("Enter username: "))
#     password=(input("Enter password: "))

# sent=input("Enter a sentence: ")
# vowels="aeiouAEIOU"
# vowel_count=0
# consonant_count=0
# for chr in sent:
#     if vowels.find(chr)!=-1: # it will check if the character is a vowel or not by checking if it is present in the vowels string and if it is present then it will return the index of the character in the vowels string and if it is not present then it will return -1
#         vowel_count+=1
#     else:
#         consonant_count+=1
# print("The number of vowels in the sentence is: ", vowel_count)
# print("The number of consonants in the sentence is: ", consonant_count)

# name="siddharth" 
# vowel="aeiouAEIOU"
# cons_count=0
# vowels_count=0
# for i in name:
#     if i in  vowel:
#         vowels_count+=1
#     else:
#         cons_count+=1
# print("The number of vowels in the name is: ", vowels_count)
# print("The number of consonants in the name is: ", cons_count)




# # remove of all occurence of an elemnt from a list
# list=[1,2,3,4,5,2,3,2]
# print(list)
# element=int(input("Enter an element to remove: "))
# for i in list:
#     if i==element:
#         list.remove(i) # it will remove the first occurrence of the element from the list and if there are multiple occurrences of the element in the list then it will only remove the first occurrence and not all the occurrences
# print(list)




# list=[1,2,3,4,5,2,3,2]
# print(list)
# product=1
# for i in list:
#     product*=i
# print("The product of all the elements in the list is: ", product)




# ---------------- File handling-----------------
# why we use file handling in python?
# File handling allows us to read from and write to files, which is essential for data persistence and manipulation. 
# It enables us to store data in a structured format, 
# share data between different programs, and perform various operations on files such as reading, writing, appending, and deleting.
#  File handling is crucial for tasks like data analysis, logging, and managing large datasets that cannot be stored in memory.

# f=open("myFile.txt",'w') # it will create a new file named myFile.txt in the current directory and open it in write mode and if the file already exists then it will overwrite the existing file
# print("name of the file:",f.name) # it will print the name of the file
# print("mode of the file:",f.mode) # it will print the mode in which the file is opened
# print("is the file readable?",f.readable()) # it will check if the file is readable or not and return True or False
# print("is the file writable?",f.writable()) # it will check if the file is writable or not and return True or False
# print("is the file closed?",f.closed) # it will check if the file is closed or not and return True or False
# print("is the file closed?",f.closed) # it will check if the file is closed or not and return True or False
# f.write("helloworld") # it will write the string "helloworld" to the file
# f.close() # it will close the file and release the resources associated with the file
# print("is the file closed?",f.closed) # it will check if the file is closed or not and return True or False

# Appending to a file
# f=open("myFile.txt",'a') # it will open the file in append mode
# f.write("\n Siddharth will be the bestest guy you all ever see") # it will write the string "Siddharth will be the bestest guy you all ever see" to the file
# f.write("\n Om has big ass") # it will write the string "Om has big ass" to the file
# f.write("\n Maruti has big nose") # it will write the string "Maruti has big nose" to the file
# f.write("\n Siddharth has big brain") # it will write the string "Siddharth has big brain" to the file
# f.close() # it will close the file and release the resources associated with the file
# print("File has been written successfully.")

# writing a list, dictionary and tuple to a file using writelines() method
# f=open("myFile.txt",'w') # it will open the file in write mode
# mylist=["Siddharth is a good boy\n", "Om is a bad boy\n", "Maruti is a good boy\n"]
# f.writelines(mylist)
# mydict={"name": "Siddharth", "age": 22, "city": "Sawantwadi"}
# f.writelines(mydict) # it will write the string representation of the dictionary to the file
# mytuple=("Siddharth", 22, "Sawantwadi")
# f.writelines(str(mytuple)) # it will write the string representation of the tuple to the file
# f.close()
# print("File has been written successfully.")



# Reading from a file
# f=open("myFile.txt",'r') # it will open the file in read mode
# print(f.read()) # it will read the entire content of the file and return it as a string
# f.close() # it will close the file and release the resources associated with the file   


# with open("myFile.txt",'a') as f: # it will open the file in append mode and automatically close the file after the block of code is executed
#     f.write("\n wow siddharth.") # it will write the string "This is a new line added to the file using with statement." to the file
#     f.write("\n How gross Om")
#     f.write("\n How smelly Maruti.")
#     print("is file closed",f.closed)
# print("is file closed",f.closed)

# with open("myFile.txt",'r') as f: # it will open the file in read mode and automatically close the file after the block of code is executed
#     content=f.read()
#     print("The file content is:",content)


# f1=open("hulk.jpg",'rb') # it will open the file in binary read mode
# f2=open("marvel_hulk.jpg",'wb') # it will open the file in binary write mode
# data=f1.read() # it will read the entire content of the file and return it as a bytes object
# f2.write(data) # it will write the bytes object to the file
# print("File has been copied successfully.")



# csv full form is comma separated values. It is a file format that is used to store tabular data in a plain text format.
#  Each line in a CSV file represents a row of data, and each value in the row is separated by a comma. 
# CSV files are commonly used for data exchange between different applications and for storing data in a simple and human-readable format.


# import csv
# f=open("stdent.csv","a",newline="") # it will open the file in append mode and newline="" is used to avoid adding an extra newline character after each row
# a=csv.writer(f) # it will create a csv writer object that will be used to write data to the file
# # a.writerow(['StudentId','Roll_No.','Name','Mobile_No.'])
# studentId=int(input("Enter student id: "))
# Roll_No=input("Enter roll number: ")
# Name=input("Enter name: ")
# Mobile_No=int(input("Enter mobile number: "))
# a.writerow([studentId,Roll_No,Name,Mobile_No]) # it will write the list of values as a row in the csv file
# print("Data has been written to the file successfully.")





import csv
import email
f=open("student1.csv","a",newline="")
a=csv.writer(f)
a.writerow(['roll_no','name','mobile_no','p1','p2','p3','total','percentage','email','result'])
roll_no=int(input("Enter roll number: "))
name=input("Enter name: ")  
mobile_no=int(input("Enter mobile number: "))
p1=int(input("Enter marks of subject 1: "))
p2=int(input("Enter marks of subject 2: ")) 
p3=int(input("Enter marks of subject 3: "))
total=p1+p2+p3
percentage=total/3
email=input("Enter email: ")
if p1>=40 and p2>=40 and p3>=40:
    result="Pass"
else:
    result="Fail"
a.writerow([roll_no,name,mobile_no,p1,p2,p3,total,percentage,email,result])
print("Data has been written to the file successfully.")