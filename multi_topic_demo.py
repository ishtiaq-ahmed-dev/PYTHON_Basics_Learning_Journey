"""
multi_topic_demo.py

A collection of foundational Python demonstrations: loops, patterns, input processing, 
and practical applications (ATM and a simple game).
"""

from random import randint

# --- 1. Loop Demonstrations ---

def demonstrate_while_loops():
    """Demonstrates simple and nested while loops."""
    print("--- 1. WHILE Loop Demonstrations ---")
    
    # A. Stepped While Loop
    try:
        a = int(input("Enter starting value for loop (a): "))
        b = int(input("Enter ending value for loop (b): "))
        
        current = a
        print(f"\nA. Counting from {a} to {b} in steps of 5:")
        while current <= b:
            print(current)
            current += 5
    except ValueError:
        print("Error: Please enter whole numbers for loop range.")
        
    # B. Nested While Loop (Simple Grid)
    print("\nB. Nested While Loop (i, j grid):")
    i = 0
    while i < 3:  # Reduced range for cleaner output
        j = 1
        while j < 5:
            print(f"({i}, {j})", end=" ")
            j += 1
        print()
        i += 1 

# --- 2. Pattern Printing ---

def print_patterns(n=5):
    """Demonstrates printing simple patterns using nested for loops."""
    print("\n--- 2. Pattern Printing ---")
    
    # A. Decreasing Right Triangle
    print("\nA. Decreasing Right Triangle:")
    for i in range(n):
        print("* " * (n - i))
        
    # B. Right-Aligned Increasing Triangle
    print("\nB. Right-Aligned Increasing Triangle:")
    for i in range(n):
        # Print leading spaces
        print("  " * (n - i - 1), end="")
        # Print stars
        print("* " * (i + 1))

# --- 3. Percentage and String Operations ---

def student_enrollment_and_initials():
    """Calculates student enrollment percentage and generates initials."""
    print("\n--- 3. Enrollment and Initials ---")
    
    # A. Enrollment Percentage
    try:
        total = int(input("Enter total registered students: "))
        males = int(input("Enter number of males: "))
        females = int(input("Enter number of females: "))
        
        if total == 0:
            print("Cannot calculate percentage for 0 students.")
        elif males + females > total:
            print("ERROR: Males and females count exceeds total students.")
        else:
            male_percentage = (males / total) * 100
            female_percentage = (females / total) * 100
            print(f"Male percentage: {male_percentage:.2f}%")
            print(f"Female percentage: {female_percentage:.2f}%")
    except ValueError:
        print("Error: Please enter whole numbers for counts.")
    except ZeroDivisionError:
        print("Error: Total registered students cannot be zero.")

    # B. Initials Generator
    first_name = input("Enter first name: ").strip().capitalize()
    last_name = input("Enter last name: ").strip().capitalize()
    
    if first_name and last_name:
        initials = first_name[0] + last_name[0]
        print(f"Initials: {initials}")
    else:
        print("Could not generate initials. Ensure both names are entered.")


# --- 4. ATM Simulator ---

def run_atm_simulator(initial_balance=100.00):
    """
    Simulates a basic ATM with check balance, deposit, and withdraw functions.
    """
    print("\n--- 4. ATM Simulator ---")
    print("Welcome! Your initial balance is: $100.00")
    
    balance = initial_balance
    menu = (
        "\nMENU:\n"
        "-> Type 'check balance'\n"
        "-> Type 'deposit'\n"
        "-> Type 'withdraw'\n"
        "-> Type 'exit'"
    )

    while True:
        print(menu)
        choice = input("Please type your choice: ").lower().strip()
        
        if choice == "check balance":
            print(f"Your current balance is: ${balance:,.2f}")
            
        elif choice == "deposit":
            try:
                amount = float(input("Enter the amount you want to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposit successful. Your new balance is: ${balance:,.2f}")
                else:
                    print("Error: Deposit amount must be positive.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                
        elif choice == "withdraw":
            try:
                amount = float(input("Enter the withdrawal amount: "))
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive.")
                elif amount <= balance:
                    balance -= amount
                    print(f"Withdrawal successful. Your new balance is: ${balance:,.2f}")
                else:
                    print("Insufficient balance or error.")
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")

        elif choice == "exit":
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Error: Invalid choice.")


# --- 5. Simple Game (Rock-Paper-Scissors/Elemental) ---

def run_elemental_game():
    """
    Simulates a simple two-player game (e.g., Ice/Water/Fire battle).
    The logic is simplified and corrected using a dict for victory conditions.
    """
    print("\n--- 5. Elemental Battle (Ice: 1, Water: 2, Fire: 3) ---")
    
    player_1_health = 10
    player_2_health = 10
    
    # Define victory conditions: (Attacker: Loser)
    # 1 (Ice) > 3 (Fire), 2 (Water) > 1 (Ice), 3 (Fire) > 2 (Water)
    WIN_CONDITIONS = {
        '1': '3',  # Ice beats Fire
        '2': '1',  # Water beats Ice
        '3': '2'   # Fire beats Water
    }

    while player_1_health > 0 and player_2_health > 0:
        print(f"\nP1 Health: {player_1_health} | P2 Health: {player_2_health}")
        
        # Player 1's turn
        weapon_1 = input("P1: Enter your weapon mode (1, 2, or 3): ").strip()
        
        # Player 2's turn (Computer)
        weapon_2 = str(randint(1, 3))
        
        if weapon_1 not in ['1', '2', '3']:
            print("P1: Invalid weapon choice. Turn skipped.")
            continue
            
        print(f"P1 chose {weapon_1}, P2 chose {weapon_2}")

        if weapon_1 == weapon_2:
            print("TIE! No damage.")
            
        # Check if P1 wins
        elif WIN_CONDITIONS.get(weapon_1) == weapon_2:
            print("PLAYER 1 WINS the round!")
            player_2_health -= 1
        
        # Check if P2 wins (P1 loses)
        else:
            print("PLAYER 2 WINS the round!")
            player_1_health -= 1

    print("\n--- GAME OVER ---")
    if player_2_health <= 0:
        print("CONGRATULATIONS! Player 1 is the WINNER!")
    elif player_1_health <= 0:
        print("CONGRATULATIONS! Player 2 is the WINNER!")

