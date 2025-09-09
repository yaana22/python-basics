# Accept list elements from the user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Check if the list is sorted
if nums == sorted(nums):
    print("List is sorted in ascending order.")
elif nums == sorted(nums, reverse=True):
    print("List is sorted in descending order.")
else:
    print("List is not sorted.")






































