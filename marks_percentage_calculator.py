"""
marks_percentage_calculator.py

Calculates a student's percentage based on marks entered over a loop.
"""

def calculate_student_percentage(number_of_papers=7):
    """
    Collects marks for a specified number of papers, calculates total marks, 
    and determines the final percentage.
    """
    print("--- Student Percentage Calculator ---")
    total_obtained_marks = 0
    
    try:
        # Use a list to store marks for later analysis (professional practice)
        marks_list = []
        
        for i in range(1, number_of_papers + 1):
            # Enforce integer input for marks
            marks = int(input(f"Please enter your marks for Paper {i}: "))
            if marks < 0:
                raise ValueError("Marks cannot be negative.")
                
            marks_list.append(marks)
            total_obtained_marks += marks

        # Get total possible marks
        total_possible_marks = int(input("\nPlease enter the total possible marks for all papers: "))
        
        if total_possible_marks <= 0:
            print("\nERROR: Total possible marks must be a positive number.")
            return

        percentage = (total_obtained_marks / total_possible_marks) * 100
        
        print("\n--- Results ---")
        print(f"Marks obtained across {number_of_papers} papers: {marks_list}")
        print(f"Your total obtained marks are: {total_obtained_marks}")
        print(f"Total possible marks: {total_possible_marks}")
        # Format percentage to two decimal places
        print(f"Your final percentage is: {percentage:.2f}%")

    except ValueError as e:
        print(f"\nERROR: Invalid input. Please ensure all inputs are valid whole numbers. ({e})")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_student_percentage(number_of_papers=5) # Reduced number of papers for quick testing