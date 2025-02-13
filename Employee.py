class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def send(self):
        print(f"Employee name is {self.name}, Salary is {self.salary}")

emp = Employee("Pradeep", 50000)

emp.send()
