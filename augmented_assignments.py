"""
augmented_assignments.py

Demonstrates Python's augmented assignment operators for arithmetic operations.
These operators combine an operation with the assignment of a result (e.g., x = x + 5 becomes x += 5).
"""

def demonstrate_augmented_assignments():
    """
    Performs and prints the results of various augmented assignment operations.
    """
    print("--- Augmented Assignment Operators Demonstration ---")
    
    # Use 'value' as a clear, reusable variable name
    value = 10
    print(f"Starting value (value = 10)")

    # 1. Addition Assignment (+=)
    value += 5
    print(f"1. Addition Assignment (value += 5): value is now = {value}") 

    # 2. Subtraction Assignment (-=)
    value -= 20
    print(f"2. Subtraction Assignment (value -= 20): value is now = {value}") 

    # 3. Multiplication Assignment (*=)
    value = 25 # Reset for clarity
    value *= 2
    print(f"3. Multiplication Assignment (value *= 2): value is now = {value}") 

    # 4. Division Assignment (/=)
    value = 17
    value /= 5
    print(f"4. True Division Assignment (value /= 5): value is now = {value}") 

    # 5. Modulus (Remainder) Assignment (%=)
    value = 13
    value %= 3
    print(f"5. Modulus Assignment (value %= 3): value is now = {value}") 

    # 6. Exponential Assignment (**=)
    value = 2
    value **= 3
    print(f"6. Exponential Assignment (value **= 3): value is now = {value}") 
    
    # 7. Floor Division Assignment (//=)
    value = 10
    value //= 3
    print(f"7. Floor Division Assignment (value //= 3): value is now = {value}") 

