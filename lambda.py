def calculateBonus(salary):
    return salary*0.05

calculate = lambda salary: salary*0.05

print(calculateBonus(200000))
print(calculate(200000))

calculatePrice = lambda price, quantity: (price*quantity)

print(calculatePrice(1500, 6))

def findNumber(number):
    if(number %2 == 0):
        print("Even")
    else:
        print("ODD")

findNumber(20)

result = lambda number: "Even" if number %2 ==0 else "odd"
print(result(20))