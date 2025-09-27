"""
range_and_for_loops.py

Demonstrates various uses of the Python 'for' loop and the 'range()' function, 
as well as a fixed conditional logic example.
"""

def evaluate_number_condition():
    """
    Fixes the complex conditional logic from the original file (where a>10 and a<10 
    could not logically be true together) into a functional if-elif-else ladder.
    """
    print("\n--- 1. Fixed Conditional Logic Demo ---")
    try:
        a = float(input("Enter a number: "))
        
        # Using a logical if-elif-else structure
        if a > 10:
            print("Output: The number is greater than 10 ('null')")
        elif a < 10:
            # Note: The original code intended to check for specific smaller values, 
            # so we check if it is non-positive here.
            if a == 0:
                 print("Output: The number is zero ('by by')")
            elif a < 0:
                 print("Output: The number is negative ('out')")
            else:
                 print("Output: The number is positive but less than 10 ('hi')")
        else: # a must be exactly 10
            print("Output: The number is exactly 10 ('out')")
            
    except ValueError:
        print("ERROR: Invalid input. Please enter a number.")


def demonstrate_range():
    """Demonstrates basic, stepped, and reverse range usage."""
    print("\n--- 2. Range Function Demonstrations ---")
    
    # Basic Range (1 to 9)
    print("A. Counting 1 to 9 (range(1, 10)):")
    for x in range(1, 10):
        print(x, end=" ")
    print("\n")
    
    # Reverse Range (10 down to 2)
    print("B. Counting 10 down to 2 (range(10, 1, -1)):")
    for x in range(10, 1, -1):
        print(x, end=" ")
    print("\n")
    
    # Stepped Range (2, 4, 6... up to 18)
    print("C. Counting in steps of 2 (range(2, 20, 2)):")
    for x in range(2, 20, 2):
        print(x, end=" ")
    print("\n")


def multiplication_and_custom_range():
    """Demonstrates creating a table and a user-defined stepped range."""
    print("\n--- 3. Multiplication and Custom Range ---")
    
    # Multiplication Table Example
    print("A. Multiplication Table (x * 2):")
    for x in range(2, 11):
        print(f"{x} multiply by 2 is : {x*2}")

    # Custom Stepped Range (Forward)
    try:
        start = int(input("\nB. Custom Range - Enter the starting value: "))
        end = int(input("Enter the ending value: "))
        step = int(input("Enter the step size you want: "))
        
        if step <= 0:
            print("ERROR: Step size must be positive for a forward range.")
            return

        print(f"Counting from {start} to {end} in steps of {step}:")
        for x in range(start, end, step):
            print(x)
            
    except ValueError:
        print("ERROR: Please enter whole numbers for all inputs.")

    # Custom Stepped Range (Reverse)
    try:
        start_rev = int(input("\nC. Custom Reverse Range - Enter the starting value (e.g., 30): "))
        end_rev = int(input("Enter the ending value (e.g., 5): "))
        step_rev = int(input("Enter the negative step size (e.g., 3): "))
        
        if step_rev >= 0:
            print("ERROR: Step size must be negative for a reverse range.")
            return

        print(f"Counting from {start_rev} down to {end_rev} in steps of {step_rev}:")
        for x in range(start_rev, end_rev, step_rev):
            print(x)
            
    except ValueError:
        print("ERROR: Please enter whole numbers for all inputs.")


if __name__ == "__main__":
    evaluate_number_condition()
    demonstrate_range()
    multiplication_and_custom_range()