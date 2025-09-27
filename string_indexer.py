"""
string_indexer.py

Prompts the user for a word and demonstrates string indexing and basic string 'modification'.
"""

def demonstrate_string_indexing():
    """
    Takes a word and an index, then displays characters and demonstrates modification.
    """
    print("--- String Indexing and Modification Demo ---")
    
    # Use descriptive variable names
    original_word = input("Please enter a word: ").strip()
    word_length = len(original_word)

    if word_length == 0:
        print("Error: Word cannot be empty.")
        return

    print("\n--- Character Index Mapping ---")
    # Use a dynamic loop instead of hardcoding print statements
    for index, char in enumerate(original_word):
        print(f"Index {index}: '{char}'")
    
    # --- String Modification Demonstration (Immutability) ---
    print("\n--- Modification Demo (Creating a new string) ---")
    
    try:
        # Robustly handle index input
        location_to_change = int(input(f"Enter the index (0 to {word_length-1}) you want to change: "))
        new_char = input("What single alphabet/character do you want to insert? ").strip()
        
        if 0 <= location_to_change < word_length and len(new_char) == 1:
            # Create a new string by concatenating parts of the old string
            new_word = original_word[:location_to_change] + new_char + original_word[location_to_change + 1:]
            
            print(f"\nOriginal word: '{original_word}'")
            print(f"Modified word: '{new_word}'")
            
        else:
            print("\nERROR: Invalid index or input. Index must be within range, and the new character must be a single character.")
            
    except ValueError:
        print("\nERROR: Invalid input. Please enter a whole number for the index.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
