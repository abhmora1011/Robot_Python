# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_dollars, store))

for i in store_euros:
    print(i)
    
# EUROS
# ('shirt', 16.4)
# ('pants', 20.5)
# ('jacket', 41.0)
# ('socks', 8.2)

# DOLLARS
# ('shirt', 24.390243902439025)
# ('pants', 30.48780487804878)
# ('jacket', 60.97560975609756)
# ('socks', 12.195121951219512)
