# A company has a sales record of N products for M days .The company wishes to know the maximum revenue received froma given product of the N products each day .Write an algorithm to find the highest revenue received each day 
def maxRevenue(revenue):   #time complexity O(n)
    maxrevenue = revenue[0]   # time comlexity O(1)
    for i in range(1,len(revenue)):   #time complexity O(n)
        if revenue[i]>maxrevenue:  #time complexity O(1)
            maxrevenue=revenue[i]
    return maxrevenue

N=int(input("Enter the number of products: "))
M=int(input("Enter the number of days: "))
revenue = [] # a list to store the revenue for each product for each day
print("Enter the revenue for each product for each day:")
for i in range(M): # loop to take input for each day # time complexity O(M)
    day_revenue = []   # list to store the revenue for each product for the current day
    for j in range(N):  # loop to take input for each product for the current day # time complexity O(N)
            rev = int(input(f"Revenue for product {j+1} on day {i+1}: ")) # input for the revenue of each product for the current day f is ued to format the string to display the product number and day number
            day_revenue.append(rev) # appending the revenue of each product for the current day to the day_revenue list
    revenue.append(day_revenue)  # appending the day_revenue list to the revenue list to store the revenue for each product for each day
 
for i in range(M): # loop to find the maximum revenue for each day # time complexity O(M)
    max_rev = maxRevenue(revenue[i]) # calling the maxRevenue function to find the maximum revenue for the current day and storing it in the max_rev variable
    print(f"Maximum revenue for day {i+1}: {max_rev}") # printing the maximum revenue for each day using f string to format the string to display the day number and maximum revenue

# final time complexity of this code is O(M*N) because we are taking input for each product for each day which takes O(M*N) time and then we are finding the maximum revenue for each day which takes O(M) time and all other operations are O(1)