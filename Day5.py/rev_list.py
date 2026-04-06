def rev_list(list):
    return list[::-1]

list = input("Enter a list of items separated by spaces: ").split()
print(rev_list(list))
