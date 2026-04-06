#  crud operations in OOP
import sys
class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentId=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]
    def addStudent(self):
        id=int(input("Enter student ID: "))
        name=input("Enter student name: ")
        rollNo=int(input("Enter student roll number: "))
        city=input("Enter student city: ")
        self.studentId.append(id)
        self.studentName.append(name)
        self.studentRollNo.append(rollNo)
        self.studentCity.append(city)
        print("Student information added successfully.")
    def displayStudent(self):
        for i in range(len(self.studentId)):
            print("Student ID:", self.studentId[i])
            print("Student Name:", self.studentName[i])
            print("Student Roll Number:", self.studentRollNo[i])
            print("Student City:", self.studentCity[i])
            print()
    def updateStudent(self):
        id=int(input("Enter student ID to update: "))
        if id in self.studentId:
            index=self.studentId.index(id)
            print("what do you want to update?" \
            " 1.Name 2.Roll Number 3.City")
            choice=int(input("Enter your choice: "))
            if choice==1:
                name=input("Enter new student name: ")
                self.studentName[index]=name
            elif choice==2:
                rollNo=int(input("Enter new student roll number: "))
                self.studentRollNo[index]=rollNo
            elif choice==3:
                city=input("Enter new student city: ")
                self.studentCity[index]=city
            print("Student information updated successfully.")
        else:
            print("Student ID not found.")
        def deleteStudent(self):
            id =int(input("Enter student ID to delete:"))
            if id in self.studentId:
                index=self.studentId.index(id)
                del self.studentId[index]
                del self.studentName[index]
                del self.studentRollNo[index]
                del self.studentCity[index]
                print("Student information deleted successfully.")
            else:
                print("Student ID not found.")
obj=CRUD()
print("Enter Your Choice:" \
" 1.Add Student" \
" 2.Display Student " \
"3.Update Student " \
"4.Delete Student")
while True:

 choice=int(input("Enter your choice: "))
 if choice==1:
    obj.addStudent()
 elif choice==2:
    obj.displayStudent()
 elif choice==3:
    obj.updateStudent() 
 elif choice==4:
    obj.deleteStudent()
 elif choice==5:
    print("Exiting the program.")
    sys.exit()  
else:   
    print("Invalid choice. Please try again.")  


