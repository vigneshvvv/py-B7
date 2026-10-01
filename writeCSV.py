import csv

employees = [
    [101, "Deva", 90000],
    [102, "Kishore", 70000]
]

with open("employeeInfo.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "empName", "Salary"])
    # writer.writerow([101, "Deva", 100000])
    # writer.writerow([102, "Kishore", 70000])
    # print("File writing completed")

    writer.writerows(employees)
    

