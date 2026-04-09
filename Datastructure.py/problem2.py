# write an algorithm to help apparel to find the number of plots that it can select for its outlets
from cmath import sqrt


arr=int(input("Enter the number of plots: "))
count=0
for i in range(arr):
    num=[int(input("Enter the area of the plot: "))]
    if num == [int(sqrt(num[0])) ** 2]:
        count+=1    
print("Number of plots that can be selected for outlets:", count)
