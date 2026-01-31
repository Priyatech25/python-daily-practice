class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90: return "A"
        if self.marks >= 75: return "B"
        return "C"

s = Student("Ravi", 88)
print(s.name, s.grade())
