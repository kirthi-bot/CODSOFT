# Simple Calculator Program

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Please select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        
        # Get user input for operation choice
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            # Get user input for the two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the calculation based on the user's choice
            if choice == '1':
                result = num1 + num2
                operation = '+'
            elif choice == '2':
                result = num1 - num2
                operation = '-'
            elif choice == '3':
                result = num1 * num2
                operation = '*'
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                    continue
                result = num1 / num2
                operation = '/'

            # Display the result
            print(f"The result of {num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()

