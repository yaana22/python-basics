# Accept name and age from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Check if the user is a valid voter
if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Hello {name}, you are not a valid voter yet.")
