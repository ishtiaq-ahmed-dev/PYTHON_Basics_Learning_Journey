"""
election_simulator.py

Simulates a basic voting process for two candidates over a fixed number of votes (e.g., 20).
"""

from collections import Counter

def run_election_simulation(total_voters=20):
    """
    Runs a voting simulation for two candidates, Imran Khan and Nawaz Sharif.
    
    Args:
        total_voters (int): The total number of votes to be cast.
    """
    print("--- Election Voting Simulation ---")
    print("Candidates: Imran Khan (Type: 'imran') and Nawaz Sharif (Type: 'nawaz')")
    print(f"Total votes to be cast: {total_voters}")

    # Use a dictionary to store votes for easy scalability
    votes = Counter()

    for i in range(1, total_voters + 1):
        try:
            # Clean and normalize input for case-insensitivity
            voter_choice = input(f"Vote {i}/{total_voters} - Please enter your vote ('imran' or 'nawaz'): ").lower().strip()
            
            if voter_choice == "imran":
                votes["Imran Khan"] += 1
            elif voter_choice == "nawaz":
                votes["Nawaz Sharif"] += 1
            else:
                print("Invalid input. Please enter 'imran' or 'nawaz'. Vote skipped.")
        
        except Exception as e:
            print(f"An unexpected error occurred during voting: {e}. Vote skipped.")

    # --- Results ---
    imran_votes = votes.get("Imran Khan", 0)
    nawaz_votes = votes.get("Nawaz Sharif", 0)
    total_valid_votes = imran_votes + nawaz_votes
    
    print("\n--- Final Results ---")
    print(f"Votes for IMRAN KHAN: {imran_votes}")
    print(f"Votes for NAWAZ SHARIF: {nawaz_votes}")
    print(f"Total valid votes cast: {total_valid_votes}")

    if total_valid_votes > 0:
        if imran_votes > nawaz_votes:
            print("\nResult: IMRAN KHAN is the winner!")
        elif nawaz_votes > imran_votes:
            print("\nResult: NAWAZ SHARIF is the winner!")
        else:
            print("\nResult: The election ended in a TIE!")

if __name__ == "__main__":
    run_election_simulation(total_voters=10) # Set a smaller number of voters for easy testing