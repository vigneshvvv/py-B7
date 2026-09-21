employees = {
    "emp1":{
        "name": "Arun",
        "Dep": "Dev",
        "Skills": ["Java", "Python"]
    },
    "emp2":{
        "name": "Rahul",
        "Dep": "Testing",
        "Skills": ["ManualTesting", "RegressionTesting"]
    }
}

print(employees["emp1"]["name"])

print(employees["emp2"]["Skills"][1])

student = {
    "name": "Vignesh",
    "Dep": "EEE"
}

studentNew = {
    **student,
    "city": "Chennai"
}

print(studentNew)