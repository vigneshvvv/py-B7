students =["Dharshan\n", "kishore\n", "Arvind\n"]

with open("students.txt", "w") as file:
    # file.write("Vignesh\n")
    # file.write("Deva\n")
    # file.write("Revanth\n")
    file.writelines(students)
    print("written")