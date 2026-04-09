
# valid mobile number check

# import re
# mo=input("Enter mobile Number:+91 ")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")





# valid email id check

import re
gmail=input("Enter Gmail id: ")
obj=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com|\w[a-zA-Z0-9_.]*@ybit[.]ac[.]in",gmail)
if obj!=None:
    print("Valid Gmail id")
else:
    print("Invalid Gmail id")


