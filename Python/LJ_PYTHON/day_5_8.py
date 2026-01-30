# 8. Find the length of each city's name
# With len() method
city_lengths_with_len = tuple(len(city.strip()) for city in cities)
print(f"Lengths of city names (using len()): {city_lengths_with_len}")

# Without len() method
city_lengths_without_len = []
for city in cities:
    length = 0
    for char in city.strip():
        length += 1
    city_lengths_without_len.append(length)
print(f"Lengths of city names (without len()): {tuple(city_lengths_without_len)}")
