# str1=input("Enter the string")
# count=0
# for i in range (len(str1)-1):
#     if str1[i]==str1[i+1]:
#         count+=1
#     else:
#         print(str1[i]+str(count+1),end="")
#         count=0
# print(str1[len(str1)-1]+str(count+1),end="")


# solving above example with the help of dictionary
# str1=input("Enter the string")
# dict1={}
# for i in str1:
#     if i in dict1:
#         dict1[i]+=1 #This will add 1 to the value of the key in the dictionary if the key is already present in the dictionary
#     else:
#         dict1[i]=1
# for key,value in dict1.items(): # item() method is used to get the key and value of the dictionary
#     print(key+str(value),end="")




# Reverse each word in string
# str="Hello Everyone"
# for i in str.split(): #split() method is used to split the string into a list of words
#       print(i[::-1],end=" ")

