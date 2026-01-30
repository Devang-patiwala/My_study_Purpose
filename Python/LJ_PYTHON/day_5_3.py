# 3. Calculate the total of all marks
# With sum() method
t2 = (85, 90, 78, 92, 88)
total_with_sum = sum(t2)
print(f"Total marks (using sum()): {total_with_sum}")

# Without sum() method
total_without_sum = 0
for mark in t2:
    total_without_sum += mark
print(f"Total marks (without using sum()): {total_without_sum}")
