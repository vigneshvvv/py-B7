import csv

with open("employeeInfo.csv", "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        # if int(row["Marks"]) > 450:
        #     print(row)