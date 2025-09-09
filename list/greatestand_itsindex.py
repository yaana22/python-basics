nums = list(map(int, input("Enter numbers separated by space: ").split()))

max_val = max(nums)
index_val = nums.index(max_val)
print("Greatest element:", max_val)
print("Index of greatest element:", index_val)
