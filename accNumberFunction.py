accDetails = [
    {
        "AccNumber": 23132144241,
        "PIN_Number": 3232
    },
     {
            "AccNumber": 23132144241,
            "PIN_Number": 3232
        },
     {
        "AccNumber": 23132144241,
        "PIN_Number": 3232
    },
    {
        "AccNumber": 23132144241,
        "PIN_Number": 3232
    }

]

def CredValidation():
    attempts = 1

    while attempts > 0:
        if attempts == 4:
            print("Maximum attempts reached")
            break

        acc = int(input("Enter your account number: "))
        pinN = int(input("Enter your PIN: "))

        loggedIn = False
        for account in accDetails:
            if acc == account["AccNumber"] and pinN == account["PIN_Number"]:
                loggedIn = True
                break

        if loggedIn:
            print("logged in ")
            break
        else:
            print("Either Acc Number or PIN Number is incorrect")
            attempts += 1

def registerAccount():
    acc = int(input("Enter your acc number: "))
    pin = int(input("Enter your PIN: "))

    global accDetails

    accDetails.append({
        "AccNumber": acc,
        "PIN_Number": pin
    })

    option = int(input("Do you want to login? 1.yes 2. no: "))

    if option == 1:
        CredValidation()


option = input("Enter operation you want to perform 1. Login 2.Register account: ")

if option == "1":
    CredValidation()
elif option == "2":
    registerAccount()
else:
    print("Invalid operation..please select valid one")
    


