# search() function :if the match found anywhere in the string then it will return the match object otherwise it will return None

# findall() function : it will return a list of all the matches found in the string

# sub() function : it will replace the matched string with the given string



# search function
import re
a=input("Enter string to perform search operation: ")
mtch=re.search(a,"Python is very important language")
print(mtch)
if mtch!=None:
    print("Match found anywhere in the string:")
    print(mtch.start(),"  ",mtch.end())
else:
    print("Match not found")

