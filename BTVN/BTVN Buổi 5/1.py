arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

add_2 = [num + 2 for num in arr]

multiply_by_2 = [num * 2 for num in arr]

shift_2 = arr[2:] + arr[:2]

print("Original list:", arr)
print("Add 2:", add_2)
print("Multiply by 2:", multiply_by_2)
print("Shift 2:", shift_2)
