def isPalindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) ==0 or len(s) == 1:
        return True
    # Recursive case: check if the first and last characters are the same
    # and then check the substring that excludes those characters
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False
    
print(isPalindrome("madam"))  # Output: True
print(isPalindrome("hello"))  # Output: False
print(isPalindrome("foobar"))  # Output: False
print(isPalindrome("awesome"))  # Output: False
# Get user input
# input_string = input("Enter a string to check if it's a palindrome: ")
# # Check if the input string is a palindrome and print the result
# if isPalindrome(input_string):
#     print(f"{input_string} is a palindrome.")   
# else:
#     print(f"{input_string} is not a palindrome.")
