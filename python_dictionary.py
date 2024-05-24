# dictionary definition
book_info = {
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'publication_year': 1925,
    'genre': 'Fiction'
}

#Accessing values through script
for key, value in book_info.items():
    print(f"{key}: {value}")
# Check if a key exists in the dictionary
key_to_check = 'rating'
if key_to_check in book_info:
    print(f"\n{key_to_check} is present in the book_info dictionary.")
else:
    print(f"\n{key_to_check} is not present in the book_info dictionary.")
