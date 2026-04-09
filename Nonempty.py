dict={"A":1,"B":2,"c":3,"D":None,"E":"fIVE"}
count=0
for i in dict:
    if isinstance(dict[i], str) and dict[i].isdigit():
        print(i,":",dict[i])
        count+=1
    elif isinstance(dict[i], (int, float)) and not isinstance(dict[i], bool):
        print(i,":",dict[i])
        count+=1
print("Total non empty values in the dictionary:",count)
    