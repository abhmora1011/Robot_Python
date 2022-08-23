# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1, 11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1, 11)]
print(squares)


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

students = [100, 90, 90, 70, 60, 50, 40, 30, 0]

#   passed_students = list(filter(lambda x: x >= 60, students))
#   passed_students = [i for i in students if i >= 60]  #   This is a list comprehension
# [100, 90, 90, 70, 60]

passed_students = [i if i >= 60 else "FAILED" for i in students]    # This is another list comprehension
# [100, 90, 90, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED']

print(passed_students)


