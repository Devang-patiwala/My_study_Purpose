# 5. Check if a number is present in the tuple t3
input_number = int(input("Enter a number to check in the tuple t3: "))
found = False
for element in t3:
    if isinstance(element, tuple) and input_number in element:
        found = True
        break
if found:
    print(f"The number {input_number} is present in the tuple t3.")
else:
    print(f"The number {input_number} is not present in the tuple t3.")
