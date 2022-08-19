# duck typing = concept where the class of an object is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

    # if walk is remove/commented out it will not accept the chicken as argument on the below method catch() and the program will throw AttributeError

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, option):
        option.walk()
        option.talk()
        print("You can caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
