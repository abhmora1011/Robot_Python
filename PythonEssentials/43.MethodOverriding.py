class Animal:

    # overrided method
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    # overriding method

    def eat(self):
        super().eat() # This will call the parent eat method()
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()


# This rabbit is eating a carrot