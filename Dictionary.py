data = dict()

student = {
    "name": "Sathish",
    "age": 20,
    "city": "Chennai"
}

print(student["name"])
print(student["age"])

student["Department"] = "EEE"

print(student)

student["age"] = 21
print(student)

# print(student["Marks"])

print(student.get("marks", 0))

student.update({
     "name": "Vignesh",
     "age": 20,
     "city": "Chennai"
})

print(student)

age = student.pop("age")
print(age)
print(student)

del student["city"]
print(student)

print(student.keys())
print(student.values())

for key, value in student.items():
    print(key,value)

print(len(student))