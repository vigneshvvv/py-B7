AccNumber = 1223342342343
PinNumber = 4343

attempts = 1

while attempts > 0:
    if attempts > 3:
        print("Maximum Attempts reached")
        break
    accNum = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN Number: "))

    if accNum == AccNumber and pin == PinNumber:
        print("Pin Matched")
        break
    else:
        print(f"Either Acc Number or Pin is not correct. Attempts Remaining {3- attempts}")
        attempts += 1

        