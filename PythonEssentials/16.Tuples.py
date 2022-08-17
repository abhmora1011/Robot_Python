# Tuples = collection which is ordered and unchangeable used to group together related data

student = ("Abe", 34, "Male")

print(student.count("Bro"))
print(student.index("Male"))

for x in student:
    print(x)

if "Abe" in student:
    print("Abe is here!")

# 0
# 2
# Abe
# 34
# Male
# Abe is here!