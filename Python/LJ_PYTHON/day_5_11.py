
# 11. Segregate odd and even numbers from a tuple
numbers = tuple(map(int, input("Enter 10 numbers separated by spaces: ").split()))
odds = tuple(num for num in numbers if num % 2 != 0)
evens = tuple(num for num in numbers if num % 2 == 0)

print(f"Odd numbers: {odds}")
print(f"Even numbers: {evens}")
