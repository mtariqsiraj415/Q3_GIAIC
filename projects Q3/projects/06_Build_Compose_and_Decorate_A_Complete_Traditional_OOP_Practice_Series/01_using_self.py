# ------------------------------------- 1:Using Self ------------------------------------ #


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    def display(self):
        return (f"Name : {self.name}, Marks : {self.marks}")


student_1:Student = Student("Muhammad Shahzad",55)
student_2:Student = Student("Muhammad Zahid",95)
print(f"Student 1 Details : {student_1.display()}")
print(student_1.name,student_1.marks)
print(f"Student 2 Details : {student_2.display()}")
