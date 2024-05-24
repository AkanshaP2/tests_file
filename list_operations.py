my_list = [5, 2, 8, 1, 7]
			
my_list.append(10)							
print("After appending 10:", my_list)
popped_element = my_list.pop()					
print("Popped element:", popped_element)
print("List after popping:", my_list)

my_list.insert(2, 20)							
print("After inserting 20 at index 2:", my_list)


my_list.reverse()							
print("After reversing:", my_list)

my_list.sort()								
print("After sorting in ascending order:", my_list)

my_list.sort(reverse=True)
print("After sorting in descending order:", my_list)
