import os,sys
fname=input("Enter the name of the file: ")
if os.path.isfile(fname):
  print("File exists",fname)
  f=open(fname,"r")
else:
  print("File does not exist",fname)
  sys.exit(0)
print("The content of the file is:")
data=f.read()
print(data)



