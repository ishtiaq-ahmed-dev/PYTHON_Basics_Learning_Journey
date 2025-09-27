"""
modulus_calculator.py

Calculates the modulus (remainder) of two user-inputted numbers.
"""

def calculate_modulus():
    """
    Prompts the user for two numbers and calculates the remainder (modulus).
    Includes error handling for non-numeric input and division by zero.
    """
    print("--- Modulus Calculator (Remainder) ---")
    try:
        # Use float for flexibility, although modulus often works best with integers
        numerator = float(input("First Number (Numerator): "))
        denominator = float(input("Second Number (Denominator): "))
        
        if denominator == 0:
            print("\nERROR: Cannot perform modulus operation with a denominator of zero.")
            return

        # Calculate the modulus (remainder)
        remainder = numerator % denominator
        
        print(f"\nCalculation: {numerator} % {denominator}")
        print(f"The Modulus (Remainder) is: {remainder}")

    except ValueError:
        print("\nERROR: Invalid input. Please enter valid numerical values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_modulus()