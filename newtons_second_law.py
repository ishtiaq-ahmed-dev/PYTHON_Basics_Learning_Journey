"""
newtons_second_law.py

Calculates the net force (F = m * a) given the mass and acceleration.
"""

def calculate_force():
    """
    Prompts the user for mass and acceleration, calculates the force, 
    and prints the result with units (Newtons).
    """
    print("--- Newton's Second Law: F = m * a ---")
    try:
        # Use float() to allow for more precise measurements
        mass_kg = float(input("Enter mass (in kg): "))
        acceleration_mps2 = float(input("Enter acceleration (in m/s^2): "))
        
        if mass_kg < 0:
            print("\nWARNING: Mass is typically non-negative.")

        # Calculate force
        force_newtons = mass_kg * acceleration_mps2
        
        # Use f-strings for clear, professional output, formatted to 2 decimal places
        print(f"\nMass: {mass_kg:.2f} kg")
        print(f"Acceleration: {acceleration_mps2:.2f} m/s^2")
        print(f"The calculated net force on the body is: {force_newtons:,.2f} Newtons (N)")

    except ValueError:
        print("\nERROR: Invalid input. Please enter valid numerical values for mass and acceleration.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
