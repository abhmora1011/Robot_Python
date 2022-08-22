# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)


friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Rosee", 20)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)

# ('Rachel', 19)
# ('Monica', 18)
# ('Chandler', 21)
# ('Rosee', 20)

# wala na sila Phoebe at Joey

