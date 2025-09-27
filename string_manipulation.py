"""
Demonstrates fundamental string operations in Python, including indexing, slicing, 
concatenation, repetition, and modification.
"""

def demonstrate_string_features():
    """
    Runs several demonstrations of string manipulation techniques.
    """
    # Use descriptive variable name
    full_name = 'ishtiaq ahmed'
    
    print("--- Basic String Operations ---")
    print(f"1. Full string is: \t\t\t'{full_name}'")
    
    # Accessing characters
    print(f"2. First character (Index 0): \t\t'{full_name[0]}'")
    
    # Slicing: [start:end] (end is exclusive)
    print(f"3. Characters from 3rd to 5th (Index 2 to 4): '{full_name[2:5]}'")
    print(f"4. Characters from 3rd onward (Index 2 to end): '{full_name[2:]}'")
    
    # Repetition
    print(f"5. Print string 2 times: \t\t'{full_name * 2}'")
    
    # Concatenation
    extended_name = full_name + " khan khattak"
    print(f"6. Concatenated string: \t\t'{extended_name}'")
    
    # Modification (Strings are immutable, so this creates a new string)
    # Replaces the character at index 2 (the 'h' in 'ishtiaq') with 'e'
    modified_string = full_name[:2] + 'e' + full_name[3:]
    print(f"7. 'Modification' (ishtiaq -> iseiaq): \t'{modified_string}'")
    
    # Professional Multiline String (Example of a Help Menu)
    help_menu = """
--- Example Command Menu ---
[R]ock: Select this option for Rock
[P]aper: Select this option for Paper
[S]cissors: Select this option for Scissors
"""
    print(help_menu)

