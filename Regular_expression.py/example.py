import re
count=0
pattern=re.compile("Function")
# print(matcher)
matcher=pattern.finditer("This is a Function to find the number of Function in the given string. Function is a keyword in Python.And Function is a block of code which only runs when it is called. Function is used to perform a specific task.")
for i in matcher:
    count+=1
    print(i.start(),"...",i.end(),"...",i.group())
print("The number of occurrences:",count)

