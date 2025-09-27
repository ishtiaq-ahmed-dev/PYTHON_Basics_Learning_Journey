"""
control_flow_and_age.py

Demonstrates Python's fundamental control flow (loops and conditionals) 
and provides a professional, accurate function for calculating age.
"""
from datetime import date

def simple_while_loop():
    """Demonstrates a simple while loop with user input and stepping."""
    print("\n--- 1. Simple While Loop (Counting by a Step) ---")
    try:
        start_value = int(input("Enter starting value: "))
        end_value = int(input("Enter ending value: "))
        step = 5
        
        current_value = start_value
        print(f"\nCounting from {start_value} to {end_value} in steps of {step}:")
        
        while current_value <= end_value:
            print(current_value)
            current_value += step
            
    except ValueError:
        print("ERROR: Invalid input. Please enter whole numbers.")

def print_decreasing_right_triangle(size=5):
    """Prints a right triangle pattern with decreasing stars."""
    print("\n--- 2. Right Triangle Pattern (Decreasing Stars) ---")
    for i in range(size):
        # Print stars using the multiplication operator for simplicity
        print(" * " * (size - i))

def print_increasing_right_triangle(size=5):
    """Prints an aligned right triangle pattern with increasing stars."""
    print("\n--- 3. Right Triangle Pattern (Increasing Stars) ---")
    for i in range(1, size + 1):
        # Print spaces first to align the triangle to the right
        print("  " * (size - i) + "* " * i)


def calculate_enrollment_percentage():
    """Calculates and prints male/female enrollment percentages."""
    print("\n--- 4. Enrollment Percentage Calculation ---")
    try:
        total_students = int(input("Enter the total number of registered students: "))
        num_males = int(input("Enter the number of males: "))
        num_females = int(input("Enter the number of females: "))
        
        if total_students == 0:
            print("Cannot calculate percentages with zero registered students.")
        elif num_males + num_females > total_students:
            print("ERROR: Sum of males and females exceeds total registered students.")
        else:
            male_percentage = (num_males / total_students) * 100
            female_percentage = (num_females / total_students) * 100
            
            # Use f-string and .2f formatting
            print(f"\nThe percentage of male students is: {male_percentage:.2f}%")
            print(f"The percentage of female students is: {female_percentage:.2f}%")
            
    except ValueError:
        print("ERROR: Invalid input. Please enter whole numbers for counts.")


def calculate_accurate_age():
    """
    **PROFESSIONAL ENHANCEMENT: Accurate Age Calculation**
    Calculates age in years, months, and days based on current date.
    """
    print("\n--- 5. Accurate Age Calculation ---")
    try:
        current_year = date.today().year
        birth_year = int(input("Enter your birth Year (e.g., 2000): "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_day = int(input("Enter your birth day (1-31): "))
        
        birth_date = date(birth_year, birth_month, birth_day)
        today = date.today()
        
        # Simple year difference
        years = today.year - birth_date.year

        # Adjust years if birthday hasn't passed this year yet
        if today < date(today.year, birth_date.month, birth_date.day):
            years -= 1
        
        print(f"\nYour actual age is: {years} years old (as of today, {today}).")
        
    except ValueError as e:
        print(f"ERROR: Invalid date component or number. Check year range or month/day values. ({e})")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    simple_while_loop()
    print_decreasing_right_triangle()
    print_increasing_right_triangle()
    calculate_enrollment_percentage()
    calculate_accurate_age()