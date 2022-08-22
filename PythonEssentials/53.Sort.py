# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

#grade = lambda grades: grades[1]
age = lambda ages: ages[2]

# students.sort(key=age)                     # sorts current list
# sorted_students = sorted(students,reverse=True) # To print if reverse

#sorted_students = sorted(students, key=grade) # sorts and creates a new list
sorted_students2 = sorted(students, key=age)

for i in sorted_students2:
    print(i)

# ('Sandy', 'A', 33)
# ('Spongebob', 'B', 20)
# ('Mr.Krabs', 'C', 78)
# ('Patrick', 'D', 36)
# ('Squidward', 'F', 60)