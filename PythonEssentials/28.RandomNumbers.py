import random

x = random.randint(1, 9) # random number between 1 and 9
y = random.random() # random number between 0 and 1

print(x)
print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) # select on mylist value

print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]
random.shuffle(cards) # this will shuffle the cards list

print(cards)
