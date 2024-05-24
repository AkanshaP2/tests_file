# List of fruits
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

# Using a for loop to iterate through the list
print("List of fruits:")
for fruit in fruits:
    print(f"- {fruit}")

#combine for loop with other parameters
for fruit in fruits:
    if fruit == 'banana':
        print(f"{fruit.capitalize()}s are my favorite!")
    else:
        print(f"I like {fruit}s.")
