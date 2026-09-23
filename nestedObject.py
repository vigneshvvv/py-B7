class Coordinates:
    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng



class Address:
    def __init__(self,state, city, lat, lng):
        self.state = state
        self.city = city
        self.coordinates = Coordinates(lat,lng)


class Employee:
    def __init__(self, id, firstName,lastName,state, city, lat, lng, skills):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.address = Address(state, city,lat,lng)
        self.skills = skills


emp  =Employee(1, "Nithish", "Kumar", "TN", "Chennai", "-1.0000", "23.13231", ["Java", "Python", "C", "C++"])
print(emp.__dict__)

print(emp.address.state)
print(emp.address.coordinates.lat)
print(emp.skills[1])
