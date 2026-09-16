AccNumber = 1223342342343
PinNumber = 4343

attempts = 1

for i in range(3):
    accNumber = int(input("Enter your Acc Number: "))
    pin = int(input("Enter your pin: "))

    if accNumber == AccNumber and pin == PinNumber:
        print("Verified")
        break
    else: 
        print(f"Either Acc Number or PIN Number is incorrect. Attempts Remaining {3-attempts}")
        attempts += 1

if attempts == 4:
    print("Maximum attempts reached. please try again after sometime")