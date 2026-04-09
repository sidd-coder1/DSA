import re
obj=input("Enter any character: ")
matcher=re.finditer(obj,"a@7 Ybc#1 ")
for i in matcher:
    print(i.start(),"...",i.end(),"...",i.group())

