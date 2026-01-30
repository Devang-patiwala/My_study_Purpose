
# 10. Find an element in t4
t4 = (('reading', 'traveling', 'music'), ('Alice', 'Bob', 'Charlie'), "Bachelor's Degree")
element_to_find = input("Enter an element to search in t4: ")
found_position = None
for idx, item in enumerate(t4):
    if isinstance(item, tuple) and element_to_find in item:
        found_position = (idx, item.index(element_to_find))
        break
    elif element_to_find == item:
        found_position = idx
        break

if found_position is not None:
    print(f"Element '{element_to_find}' found at position {found_position}.")
else:
    print("Not found.")
