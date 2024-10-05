# In main

from app.operations import Addition, Subtraction, Multiplication, Division
from datetime import datetime

def display_history(history):
    if not history:
        print("No history available.")
    else:
        print("\nOptions for history:")
        print("1: Show the most recent calculation")
        print("2: Show complete history")
        choice = input("Choose an option (1 or 2): ")
        
        if choice == '1':
            print("\nMost Recent Calculation:")
            print(history[-1])
        elif choice == '2':
            print("\nComplete History:")
            for entry in history:
                print(entry)
        else:
            print("Invalid choice. Please select either 1 or 2.")
    print("\n")

def main():
    history = []
    
    print("Welcome to the Interactive Calculator CLI!")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_input = input("Enter operation (add, subtract, multiply, divide) followed by two numbers, or 'history' to view previous calculations:\n> ")

        if user_input.lower() == 'bye':
            print("Exiting the calculator. Goodbye!")
            break
        
        elif user_input.lower() == 'history':
            display_history(history)
            continue
        
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please enter an operation followed by two numbers.")
                continue
            
            operation = parts[0]
            a = float(parts[1])
            b = float(parts[2])

            if operation == 'add':
                result = Addition(a, b).compute()
            elif operation == 'subtract':
                result = Subtraction(a, b).compute()
            elif operation == 'multiply':
                result = Multiplication(a, b).compute()
            elif operation == 'divide':
                result = Division(a, b).compute()
            else:
                print("Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'.")
                continue

            print(f'The result of {operation} {a} and {b} is: {result}')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append(f"[{timestamp}] {operation.capitalize()} {a} and {b} = {result}")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == '__main__':
    main()
