class student:
    stu_id =int(input("enter student id : "))
    stu_name =str(input("enter student name : "))

    def details(self):
        print(self)
        print(f"student id is {student.stu_id}",f"Student name is {student.stu_name}")

student.details()
