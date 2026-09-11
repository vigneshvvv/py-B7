a = int(input("Enter a Number A: "))
b = int(input("Enter a number B: "))
option = int(input("Enter a operation to perform 1. Add 2. sub 3.Multiplication 4.Division"))

if option == 1:
    print(a+b)
elif option ==2:
    if a >b:
        print(a-b)
    else:
        print("Result is negative: ", a-b)
    
elif option == 3:
    print(a * b)
elif option == 4:
    print(a/b)
else:
    print("Invalid Operation")