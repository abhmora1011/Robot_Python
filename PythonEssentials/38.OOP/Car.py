# Learn the basics of POOP

class Car:

    make = None
    model = None
    year = None
    color = None

    def __init__(self, make, model, year, color): # This is a constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This is " + self.model + " is driving")

    def stop(self):
        print("This is " + self.model + " is stopped")