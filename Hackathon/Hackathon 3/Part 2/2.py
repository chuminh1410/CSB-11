def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [5, 1, 8, 92, -1, 30]

print("Original list:")
print(" ".join(str(num) for num in nums))

selection_sort(nums)

print("Sorted list:")
print(" ".join(str(num) for num in nums))
