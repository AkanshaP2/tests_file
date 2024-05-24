# example tuple with fixed info
person_info = ("Ram", 30, "Bengaluru", "Engineer", "Male", "Ram@example.com")

# Tuple length
length_person_info = len(person_info)
print("Length of person_info tuple:", length_person_info)

# Combining tuples
additional_info = ("Married", "123 Main St")
combined_info = person_info + additional_info
print("Combined tuple:", combined_info)

# Repeating tuples
repeated_info = person_info * 2
print("Repeated tuple:", repeated_info)

# Check if an element is present in a tuple
element_to_check = "Ram"		
if element_to_check in person_info:
    print(f"{element_to_check} is present in person_info tuple")
else:
    print(f"{element_to_check} is not present in person_info tuple")

element_to_check = "29"						
if element_to_check in person_info:
    print(f"{element_to_check} is present in person_info tuple")
else:
    print(f"{element_to_check} is not present in person_info tuple")
