employees = [
    {"id": 101, "name": "John", "age": 25, "Salary": 40000},
    {"id": 102, "name": "Ram", "age": 30, "Salary": 60000},
    {"id": 103, "name": "Kumar", "age": 28, "Salary": 50000},
    {"id": 103, "name": "Abdul", "age": 35, "Salary": 75000},
]

filters = list()

for emp in employees:
    if emp["Salary"] > 50000:
        filters.append(emp)


result = filter(lambda emp: emp["Salary"] > 50000, employees)
# print(list(result))

resultN = map(lambda emp: emp["name"], employees)
# print(list(resultN))

resultN1 = map(lambda emp: {**emp, "Bonus": emp["Salary"]*1.50}, employees)
# print(list(resultN1))

resultN2 = map(lambda emp: {**emp, "Salary": emp["Salary"]*1.50}, employees)
# print(list(resultN2))

result3 = sorted(employees, key=lambda emp: emp["Salary"])
# print(result3)

result4 = sorted(employees, key=lambda emp: emp["Salary"], reverse=True)
# print(result4)


result5 = max(employees, key= lambda emp: emp["Salary"])
# print(result5)

result6 = min(employees, key= lambda emp: emp["Salary"])
print(result6)

result7 = any(emp["Salary"] > 80000 for emp in employees)
print(result7)

result8 = all(emp["Salary"] > 30000 for emp in employees)
print(result8)

result9 = map(lambda emp: emp["name"], filter(lambda emp: emp["Salary"] > 50000, employees))
print(list(result9))