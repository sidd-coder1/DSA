# i want to write a program to find the number of occurrences from a sample.txt file using regular expression
# import re
# a=input("Enter the word to find: ")
# count=0
# file=open("sample.txt","r")
# matcher=re.search(a,file.read())
# if matcher:
#     count=1
#     print(matcher.start(),"...",matcher.end(),"...",matcher.group())
# print("The number of occurrences:",count)   

import re
a=input("Enter the word to find: ")
count=0
file=open("sample.txt","r")
matcher=re.finditer(a,file.read())
for i in matcher:
    count+=1
    print(i.start(),"...",i.end(),"...",i.group())
print("The number of occurrences:",count)
file.close()
