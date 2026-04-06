list=input("Enter a list of items separated by spaces: ").split()
def is_palindrome(list):
    return list == list[::-1]
if is_palindrome(list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

