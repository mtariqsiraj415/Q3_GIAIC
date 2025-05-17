class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
        

employee_1:Employee = Employee("Shahzad",100,"123-45-6789")
print(employee_1.name)
print(employee_1._salary)
# print(employee_1.__ssn)
print(employee_1._Employee__ssn)