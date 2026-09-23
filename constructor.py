class Employee:
    # id=0
    # firstName = ""
    # lastName=""

    def __init__(self, id=0, firstName=" ", lastName =""):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


employee = Employee(1, "Sathish", "kumar")
employee.id = 2
print(employee.__dict__)
print(employee.id)

employee1 = Employee()
employee1.id = 2

print(employee1.__dict__)
