# file = open("fileName", "r")

with open("students.txt", "r") as file:
    # data = file.read(3)
    # data = file.readline()
    # data1 = file.readline()
    # print(data)
    # print(data1)
    # data = file.readlines()

    # for i in data:
    #     print(i.strip())

    for line in file:
        print(line.strip())

