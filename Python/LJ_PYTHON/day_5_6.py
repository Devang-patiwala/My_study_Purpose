# 6. Tuple of fruits and search for a fruit
fruits = ("apple", "banana", "cherry", "date", "grape")
fruit_name = input("Enter a fruit name to search: ").lower()
if fruit_name in fruits:
    print(f"{fruit_name} is present in the tuple.")
else:
    print(f"{fruit_name} is not present in the tuple.")
