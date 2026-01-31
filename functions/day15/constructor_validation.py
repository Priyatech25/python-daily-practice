class User:
    def __init__(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self.age = age

u = User(20)
print(u.age)
