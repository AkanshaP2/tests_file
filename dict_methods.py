car_info = {
    'make': 'Toyota',
    'model': 'Camry',
    'year': 2022,
    'color': 'Blue'
}

# get all keys with keys() method
keys = car_info.keys()
print("Keys:", keys)

# get all values with values() method
values = car_info.values()
print("Values:", values)

# get all key value pairs with items() method
items = car_info.items()
print("Items:", items)

# update with new info with update() method
car_info.update({'transmission': 'Automatic', 'color': 'Red'})
print("\nUpdated Car Info:", car_info)

# remove key and return its value with pop() method
removed_color = car_info.pop('color')
print("\nRemoved Color:", removed_color)
print("Updated Car Info after removing 'color':", car_info)

#clear dictionary
car_info.clear()
print(“Cleared dictionary:”, car_info)
