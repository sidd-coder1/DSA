# list=[0,0,0,1,0,3,4,]
# newlist=[]
# for i in range(len(list)):
#     if list[0]==0:
#         list.pop(0)
#     else:
#         newlist.append(list[i])

# print(newlist)


# write a program to remove the leading zeros from the list and return the new list without leading zeros
list=list(map(int, input("Enter numbers: ").split()))
while list and list[0]==0:
    list.pop(0)
print(list)


