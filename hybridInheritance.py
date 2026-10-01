class Employee:
    def __init__(self, id, name):
        self.id= id
        self.name = name

class Address(Employee):
    def __init__(self, id, name, state, city):
        Employee.__init__(self,id,name)
        self.state = state
        self.city = city

class contactInfo(Employee):
    def __init__(self, id, name, mailID):
        Employee.__init__(self,id, name)
        self.mailId = mailID

class Developer(Address, contactInfo):
    def __init__(self, id, name, state, city, mailID, skills):
        Address.__init__(self,id, name, state, city)
        contactInfo.__init__(self,id,name, mailID)
        self.skills = skills

dev = Developer(1, "Arun", "TN", "Chennai", "dev@gmail.com", "Java")
print(dev.__dict__)

