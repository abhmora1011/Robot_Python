# if statements = a block of code that will execute if it's condition is true

age = int(input("How old are you? : "))

if age == 100:
    print("You are century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't born yet!")
else:
    print("You are a child!")

# How old are you? : 12
# You are a child!