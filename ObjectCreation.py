class Employee:
    id = 0
    firstName = ""
    lastName = ""


employee1 = Employee()
employee1.id = 0
employee1.firstName = "Suresh"
employee1.lastName = "Kumar"
print(employee1.__dict__)

employee2 = Employee()
employee2.id = 1
employee2.firstName = "Rahul"
print(employee2.__dict__)
