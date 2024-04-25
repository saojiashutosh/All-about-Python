# Create Student class that takes name & marks of 3 subjects as arguments in a constroctor
# Then create a method to print the average


class Student:
    def __init__(self, name, maths, sci, eng):
        self.name = name
        self.maths_marks = maths
        self.sci_marks = sci
        self.eng_marks = eng

    def average(self):
        avg = (self.maths_marks + self.sci_marks + self.eng_marks) / 3
        return avg


s1 = Student("Sachin", 56, 78, 90)
print(s1.average())
