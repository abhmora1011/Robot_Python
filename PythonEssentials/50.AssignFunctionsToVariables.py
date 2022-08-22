# This is to assign a function to a variable
# It is like creating an alias to a  function


def hello():
    print("Hello")


print("****************")
# now the function hello and hi will have the same allocation addresss
print(hello)

hi = hello # Now hello function will have also an alias hi
print(hi)
print("****************")
hi()

say = print
say("Whoa! I can't believe this works! :O")

print("Hello")
