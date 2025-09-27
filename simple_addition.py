"""
simple_addition.py

Prompts the user for two numbers and calculates their sum.
"""

def calculate_sum():
    """
    Takes two integer inputs from the user and calculates their sum.
    Includes error handling for invalid input.
    """
    print("--- Simple Addition Calculator ---")
    try:
        # Use descriptive variable names
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        
        # Calculate the sum
        total_sum = first_number + second_number
        
        print(f"\nCalculation: {first_number} + {second_number}")
        print(f"The sum of the two numbers is: {total_sum}")

    except ValueError:
        print("\nERROR: Invalid input. Please ensure both inputs are valid whole numbers (integers).")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_sum()