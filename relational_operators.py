"""
relational_operators.py

Demonstrates Python's comparison operators (relational operators) 
which return a boolean (True or False) result based on the relationship between two values.
"""

def demonstrate_comparisons():
    """
    Prompts the user for two numbers and displays the boolean result of six comparison operators.
    """
    print("--- Boolean Comparison Operators ---")
    try:
        # Use float() to allow for professional comparison of any numbers
        first_num = float(input("Enter the First Number (a): "))
        second_num = float(input("Enter the Second Number (b): "))
        
        print("\n--- Comparison Results (a vs b) ---")
        # Use f-strings for clear output format
        
        # Less Than (<)
        print(f"a < b ({first_num} < {second_num}): \t{first_num < second_num}")
        
        # Greater Than (>)
        print(f"a > b ({first_num} > {second_num}): \t{first_num > second_num}")
        
        # Less Than or Equal To (<=)
        print(f"a <= b ({first_num} <= {second_num}): \t{first_num <= second_num}")
        
        # Greater Than or Equal To (>=)
        print(f"a >= b ({first_num} >= {second_num}): \t{first_num >= second_num}")
        
        # Equal To (==)
        print(f"a == b ({first_num} == {second_num}): \t{first_num == second_num}")
        
        # Not Equal To (!=)
        print(f"a != b ({first_num} != {second_num}): \t{first_num != second_num}")

    except ValueError:
        print("\nERROR: Invalid input. Please enter valid numerical values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

