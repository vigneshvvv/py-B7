data = (10, "Python", 20.5)
print(type(data))
num = (10,)
print(type(num))

numbers = (10,20,30,40,50)
print(numbers[0])

print(numbers[1:3])

# numbers[1] = 25

print(numbers.count(30))

print(len(numbers))

print(20 in numbers)

a = (1,2,3,4,5)
b=(6,7,8,9)

c = a+b
print(c)

for num in numbers:
    print(num)


id, tech, value = data
print(tech)   

numberN = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

print(numberN[0][0])