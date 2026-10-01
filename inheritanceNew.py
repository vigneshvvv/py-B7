class Employee:
    def __init__(self, emp_id, emp_name, mobileNumber):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.mobileNumber = mobileNumber

class Developer(Employee):
      def __init__(self, emp_id, emp_name, mobileNumber,techSkills):
            super().__init__(emp_id, emp_name, mobileNumber)
            self.techSkills=techSkills

class Tester(Employee):
      def __init__(self, emp_id, emp_name, mobileNumber,frameWorks):
            super().__init__(emp_id, emp_name, mobileNumber)
            self.frameworks = frameWorks


dev = Developer(112, "Anuj", 2423423, "Python")
print(dev.__dict__)

test = Tester(113,"Dan", 223132, "JMeter")
print(test.__dict__)