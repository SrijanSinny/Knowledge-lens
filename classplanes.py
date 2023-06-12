class Plane:
    def __init__(self, color):
        self.wings = 2
        self.color = color
    def fly(self):
        print("The plane will fly")

class Jet(Plane):
    def __init__(self,color):
        super().__init__(color)
    def fly(self):
        print(f"The {self.color} jet will fly in speed")
class Passenger(Plane):
    def __init__(self, color):
        super().__init__(color)
    def fly(self):
        print(f"The {self.color} Passenger plane will fly with  pasesngers")
#objets 
plane1 = Plane("white")
plane2 = Plane("blue")
jet1 = Jet("green")
jet2 = Jet("red")
passenger1 = Passenger("Yellow")
passenger2 = Passenger("black")

plane1.fly()
plane2.fly()
jet1.fly()
jet2.fly()
passenger1.fly()
passenger2.fly()
