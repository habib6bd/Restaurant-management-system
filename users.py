from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employess = [] #database

    def add_employee(self, name, phone, email, address, age, designation, salary):
        employee = Employee(name, phone, email, address, age, designation, salary) #Employee class er 1 ti object create hobe
        self.employess.append(employee)
        print(f"{employee.name} is added !!") #employee.name or only name ek e kotha

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employess:
            print(emp.name, emp.phone, emp.email, emp.address)

ad = Admin("Habib", 23456, "habib@gmail.com", "Dhaka")
ad.add_employee("Nahid", 23456, "nahid@gmail.com", "Gazipur", 23, "Volunteer", 12000)
ad.view_employee()


