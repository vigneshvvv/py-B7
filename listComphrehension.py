# [expression for item in iterable]

numbers = [1,2,3,4,5]

result=[]

for x in numbers:
    result.append(x*2)

resultN = [x*2 for x in numbers]
print(result)
print(resultN)

result2 = [x*10 for x in numbers if x %2 == 0]
print(result2)


employees = [
    {"id": 101, "name": "John", "age": 25, "Salary": 40000},
    {"id": 102, "name": "Ram", "age": 30, "Salary": 60000},
    {"id": 103, "name": "Kumar", "age": 28, "Salary": 50000},
    {"id": 103, "name": "Abdul", "age": 35, "Salary": 75000},
]
names = [emp["name"] for emp in employees]
print(names)

result3 = [emp["name"] for emp in employees if emp["Salary"] > 50000]
print(result3)

result4 = [{**emp, "Salary": emp["Salary"]*1.50} for emp in employees]
print(result4)

result5 = ["Even" if x%2 == 0 else "Odd" for x in numbers]
print(result5)