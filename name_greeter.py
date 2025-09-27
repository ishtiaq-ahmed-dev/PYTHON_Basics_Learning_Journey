"""
name_greeter.py

Prompts the user for their first and last name and prints a professional greeting.
"""

def get_and_greet_name():
    """
    Collects first and last name from the user, cleans the input, and prints the result.
    """
    print("--- Name Input and Greeting ---")
    
    # Use .strip() to remove leading/trailing spaces and .capitalize() for consistent output
    first_name = input("Enter your first name: ").strip().capitalize()
    last_name = input("Enter your last name: ").strip().capitalize()
    
    print("\n--- Output ---")
    print(f"Your first name is: {first_name}")
    print(f"Your last name is: {last_name}")
    print(f"Hello, {first_name} {last_name}! Welcome to the script.")

if __name__ == "__main__":
    get_and_greet_name()