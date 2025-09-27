"""

Demonstrates a clear and professional structure for 'if-elif-else' conditional logic
to evaluate the value of a user-inputted number.
"""

def evaluate_number():
    """
    Prompts for a number and evaluates it against several conditions using an if/elif/else ladder.
    """
    print("--- Conditional Number Evaluator ---")
    try:
        # Use float() to handle whole numbers or decimals
        input_value = float(input("Enter a number: "))
        
        # Professional conditional structure uses elif for mutually exclusive checks
        if input_value > 10:
            print(f"Result: The number {input_value} is significantly large (greater than 10).")
        
        # Only checked if the first condition was False
        elif input_value == 10:
            print(f"Result: The number {input_value} is exactly 10.")
            
        elif input_value > 0:
            print(f"Result: The number {input_value} is a positive value less than 10.")
            
        elif input_value == 0:
            print(f"Result: The number is zero (0).")

        else: # Covers all remaining cases (input_value < 0)
            print(f"Result: The number {input_value} is negative.")
            
    except ValueError:
        print("\nERROR: Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

