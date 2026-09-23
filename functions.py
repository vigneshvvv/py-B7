def sampleFunction():
    print("SampleFunction working")

def checkUser(userName, password):
    if("Vignesh" == userName and "Vignesh" == password):
        print("Matching")
    else:
        print("UserName and password doesn't match")

def add(a, b):
    return a+b

a = sampleFunction()
print(a)

# user = input("Enter your userName: ")
# passwordN = input("Enter your password: ")
# checkUser(user, passwordN)

c = add(10,20)
print(c)
if c%2 == 0:
    print("Even Number")
else:
    print("ODD Number")
