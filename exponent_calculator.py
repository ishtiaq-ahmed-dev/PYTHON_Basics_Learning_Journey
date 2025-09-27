"""
exponent_calculator.py

A simple Python script to calculate the power of a base number (a^b).
"""

def calculate_power():
    """
    Prompts the user for a base number and an exponent, then calculates and prints the result.
    Includes error handling for non-integer inputs.
    """
    print("--- Exponential Calculation (Base ** Exponent) ---")
    try:
        # Use descriptive variable names
        base_number = int(input("Enter the base number: "))
        exponent_value = int(input("Enter the exponent (power value): "))
        
        # Calculate the result using the built-in operator
        result = base_number ** exponent_value
        
        print(f"\nCalculation: {base_number} ** {exponent_value}")
        # Use f-string for clear output
        print(f"The result is = {result:,.0f}") # Format large results with commas

    except ValueError:
        print("\nERROR: Invalid input. Please ensure both inputs are valid whole numbers (integers).")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
