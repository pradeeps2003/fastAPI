students = []

def create():
    stu_id = int(input("enter the student id: "))
    stu_name = str(input("enter the student name: "))
    stu_age = int(input("enter the student age: "))

    student = {
        'id': stu_id,
        'name': stu_name,
        'age': stu_age
    }

    students.append(student)
    print("Details added successfully ...")

def read():
    print("Student details....", students)

def update():
    new_id = int(input("Enter id to update: "))
    for student in students:
        if new_id == student['id']:
            new_name = input("Enter the new name: ")
            student['name'] = new_name
            print("Updated successfully ....", student)
        else:   
            print("ID not found.")

def delete():
    remove_id = int(input("Enter id to remove: "))
    for student in students:
        if remove_id == student['id']:
            student.clear()
            print("Deleted successfully:")
            print(student)
            return
    print("ID not found.")
    

create()
read()
update()
delete()