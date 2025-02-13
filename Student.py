class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def validate(self):
        if self.mark >= 35 and self.mark <= 100:
            print(f"{self.name} Passed")
        else:
            print(f"{self.name} Failed")

student = Student("Pradeep", 40)
student.validate()
