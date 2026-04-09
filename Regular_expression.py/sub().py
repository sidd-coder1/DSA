# we pass three arguments 
# 1.expression: it is the regular expression that we want to search for in the string
# 2.string: it is the string in which we want to search for the regular expression
# 3.replacement string: it is the string that we want to replace the regular expression with in the string
# the re.sub() function will return a new string with the regular expression replaced by the replacement



# import re
# obj=re.sub('[0-9]','X',"2235 abcde@#$%^&*()")
# print(obj)


# subn() function : it is similar to sub() function but it will return a tuple containing the new string and the number of replacements made

import re
obj=re.subn('[0-9]','@',"2235 abcde@#$%^&*()")
print(obj)
print("The string is=",obj[0])
print("The number of replacements made=",obj[1])