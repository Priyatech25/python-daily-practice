class Bird:
    def sound(self):
        print("Some sound")

class Crow(Bird):
    def sound(self):
        print("Caw Caw")

for b in [Bird(), Crow()]:
    b.sound()
