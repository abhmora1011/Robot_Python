# Method chaining = calling multiple methods sequentially each call performs an action on the same object and return self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self     # need to declare this to trigger the method chaining

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

car.turn_on().drive()
car.brake().turn_off()
car.turn_on().drive().brake().turn_off()
print("------------------------")
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

# You start the engine
# You drive the car
# You step on the brakes
# You turn off the engine
# You start the engine
# You drive the car
# You step on the brakes
# You turn off the engine
# ------------------------
# You start the engine
# You drive the car
# You step on the brakes
# You turn off the engine
