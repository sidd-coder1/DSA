# write an algorithm to help the agency find the number of special char and whitespaces in give message

str=input("Enter the message: ")
special_char=""
count=0
for chr in str:
    if chr in "!@#$%^&*()-+":
        special_char += chr
        count += 1
print("Special characters:", special_char)
print("Count:", count)
