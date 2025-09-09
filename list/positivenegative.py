# Accept list elements from the user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("Positive elements:")
for n in nums:
    if n > 0:
        print(n, end=" ")

print("\nNegative elements:")
for n in nums:
    if n < 0:
        print(n, end=" ")
