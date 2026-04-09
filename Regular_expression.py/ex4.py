# match() it always search in the beginning
# import re
# a=input("Enter string to perform match operation: ")
# mtch=re.match(a,"Python is very important language")
# print(mtch)
# if mtch!=None:
#     print("Match found at begining level:")
#     print(mtch.start(),"  ",mtch.end())
# else:
#     print("Match not found")




# fullmatch() it always search for the full string,as a name suggest when we have to match full string with the given pattern then we can use fullmatch() method.

import re
a=input("Enter string to perform fullmatch operation: ")
mtch=re.fullmatch(a,"Python is very important language")
print(mtch)
if mtch!=None:
    print("Match found at full level:")
    print(mtch.start(),"  ",mtch.end())
else:
    print("Match not found")


