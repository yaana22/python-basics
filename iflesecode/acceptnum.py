# Accept two numbers from the user and print the greatest 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare and print the greatest
if num1 > num2:
    print(f"The greatest number is {num1}")
elif num2 > num1:
    print(f"The greatest number is {num2}")
else:
    print("Both numbers are equal.")