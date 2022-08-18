# Dictionaries = A changeable, unordered collection of unique key:value pairs
# Fast  because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'}) # To add another key value pair
capitals.update({'USA': 'Las Vegas'}) # to change the existing value
capitals.pop('China') # To delete a value
# capitals.clear()

print(capitals['Germany']) # to access the value of Germany
print(capitals.get('Germany')) # to get the value of Germany
print(capitals.keys()) # to print the keys
print(capitals.values()) # To print the values
print(capitals.items()) # To see the full dictionary declaration

for key, value in capitals.items():
    print(key, value)


# Berlin
# Berlin
# dict_keys(['USA', 'India', 'Russia', 'Germany'])
# dict_values(['Las Vegas', 'New Dehli', 'Moscow', 'Berlin'])
# dict_items([('USA', 'Las Vegas'), ('India', 'New Dehli'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])
# USA Las Vegas
# India New Dehli
# Russia Moscow
# Germany Berlin