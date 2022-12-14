# set =  collection which is unordered, un-indexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin") # add napkin to the set
print(utensils)

utensils.remove("fork") # remove the fork
print(utensils)
print(dishes)
print("******************")

# utensils.clear() # clear the set
# print(utensils)

dishes.update(utensils) # add set to another set
print(utensils)
print(dishes)

print("******************")

dinner_table = utensils.union(dishes) # combine the sets but the similar value will be merged as one
print(dinner_table)
print(dishes.difference(utensils)) # to check what are the difference
print(utensils.intersection(dishes)) # to check what is the similarity of two sets

for x in utensils:
    print(x)
