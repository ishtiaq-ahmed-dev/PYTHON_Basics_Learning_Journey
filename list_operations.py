"""
list_operations.py

Demonstrates fundamental and advanced operations on Python lists, including:
creation, slicing, comparison, and practical lookup applications.
"""

def demonstrate_basics():
    """Demonstrates list creation, types, length, and indexing."""
    print("--- 1. List Fundamentals ---")
    
    fruit_list = ["apple", "banana", "orange"]
    print(f"Original list: {fruit_list}")
    print(f"List length: {len(fruit_list)}")
    print(f"Element at index 0: {fruit_list[0]}")
    print(f"Last element (using negative index): {fruit_list[-1]}")
    
    mixed_list = ["orange", 1, True]
    print(f"Lists can contain mixed data types: {mixed_list}")

    # Slicing
    sample_list = ["apple", "banana", "orange", "cherry", "mango"]
    print(f"List slicing (index 1 to 4): {sample_list[1:4]}")


def compare_lists_by_index():
    """Compares two lists element-by-element and finds the percentage of matches."""
    print("\n--- 2. Advanced List Comparison (Element-wise Match) ---")
    
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    # Use zip() to safely iterate through both lists up to the length of the shortest one
    comparisons = [(x, y) for x, y in zip(list1, list2)]
    match_count = sum(1 for x, y in comparisons if x == y)
    total_compared = len(comparisons)
    
    if total_compared > 0:
        percentage = (match_count / total_compared) * 100
        print(f"Total items compared: {total_compared}")
        print(f"Number of exact matches (by index): {match_count}")
        print(f"Percentage of matching values: {percentage:.2f}%")
    else:
        print("Cannot compare empty lists.")


def student_marks_lookup():
    """Demonstrates list lookups using names and roll numbers."""
    print("\n--- 3. Student Marks Lookup ---")
    
    student_names = ["ali", "hamza", "khan", "khattak"]
    student_marks = [10, 30, 20, 40]
    roll_numbers = [101, 102, 103, 104]

    # Lookup by Name
    try:
        search_name = input("Enter student name for marks lookup: ").lower().strip()
        
        if search_name in student_names:
            index = student_names.index(search_name)
            marks = student_marks[index]
            print(f"--> {search_name.capitalize()} got {marks} marks.")
        else:
            print(f"--> '{search_name.capitalize()}' Not Found in the student list.")
            
    except Exception as e:
        print(f"An error occurred during name lookup: {e}")

    # Lookup by Roll Number
    try:
        search_roll = int(input("Enter roll number for marks lookup: "))
        
        if search_roll in roll_numbers:
            index = roll_numbers.index(search_roll)
            mark = student_marks[index]
            print(f"--> Roll No. {search_roll} got {mark} marks.")
        else:
            print(f"--> Roll No. {search_roll} Not Found.")
            
    except ValueError:
        print("ERROR: Invalid input for roll number. Please enter a whole number.")
    except Exception as e:
        print(f"An error occurred during roll number lookup: {e}")

if __name__ == "__main__":
    demonstrate_basics()
    compare_lists_by_index()
    student_marks_lookup()