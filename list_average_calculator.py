"""
list_average_calculator.py

Calculates the average of a predefined list of numbers.
"""

def calculate_average_of_numbers():
    """
    Defines a list of numbers, calculates their sum and average, and prints the result.
    """
    # Use a descriptive list for the numbers. This is more professional than individual variables.
    numbers = [59, 60, 75, 86, 60]
    
    count = len(numbers)
    
    if count > 0:
        # Use built-in Python functions for efficiency and readability
        total_sum = sum(numbers)
        average = total_sum / count
        
        print("--- Average Calculation ---")
        print(f"Numbers used for calculation: {numbers}")
        print(f"Total Sum: {total_sum}")
        print(f"Count of numbers: {count}")
        # Format output to two decimal places
        print(f"The calculated average is: {average:.2f}")
    else:
        print("The list of numbers is empty; cannot calculate an average.")

