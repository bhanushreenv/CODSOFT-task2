def calculator():
    print("Welcome to Simple Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose an operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation. Please choose from +, -, *, /")
                continue

            print(f"Result: {num1} {operation} {num2} = {result}")

            choice = input("Do you want to perform another calculation? (yes/no): ").lower()
            if choice != 'yes':
                print("Thank you for using Simple Calculator!")
                break

        except ValueError:
            print("Error: Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()
