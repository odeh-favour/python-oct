# Simple Python Calculator

print("--- SIMPLE CALCULATOR ---")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if choice is one of the valid options
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")

    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")

    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")

    elif choice == '4':
        if num2 == 0.0:
            print("Error! Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid Input! Please choose a valid option between 1 and 4.")