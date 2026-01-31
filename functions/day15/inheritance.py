class Person:
    def show(self):
        print("Person class")

class Employee(Person):
    def work(self):
        print("Employee working")

e = Employee()
e.show()
e.work()
