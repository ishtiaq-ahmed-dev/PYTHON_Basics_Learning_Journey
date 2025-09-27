"""
age_time_converter.py

Converts an age in years into months, days, hours, minutes, and seconds.
(Note: Uses approximate, non-leap-year conversion factors for simplicity.)
"""

# Define constants for clarity and maintainability
MONTHS_PER_YEAR = 12
DAYS_PER_YEAR_APPROX = 365.25  # Using 365.25 to account for leap years is more professional
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def convert_age_to_time_units():
    """
    Takes a user's age in years and converts it into various time units.
    """
    print("--- Age Conversion Tool (Approximate) ---")
    
    try:
        # Enforce integer input
        age_in_years = int(input("Enter your age in full years: "))
        
        if age_in_years < 0:
            print("ERROR: Age cannot be negative.")
            return

        # Calculate in sequence
        age_in_months = age_in_years * MONTHS_PER_YEAR
        # Calculating days directly from years for better accuracy than * 30 * 12
        age_in_days_approx = age_in_years * DAYS_PER_YEAR_APPROX
        age_in_hours_approx = age_in_days_approx * HOURS_PER_DAY
        age_in_minutes_approx = age_in_hours_approx * MINUTES_PER_HOUR
        age_in_seconds_approx = age_in_minutes_approx * SECONDS_PER_MINUTE

        # Use f-strings and thousands separators (commas) for professional, readable output
        print("\n--- Results (Approximate) ---")
        print(f"You are {age_in_months:,.0f} months old")
        print(f"You are {age_in_days_approx:,.0f} days old")
        print(f"You are {age_in_hours_approx:,.0f} hours old")
        print(f"You are {age_in_minutes_approx:,.0f} minutes old")
        print(f"You are {age_in_seconds_approx:,.0f} seconds old")

    except ValueError:
        print("\nERROR: Invalid input. Please enter a whole number (integer) for your age.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
