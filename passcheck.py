import re
import math
import time
import sys
from tqdm import tqdm

# CHARACTER SETS
LOWERCASE = 26
UPPERCASE = 26
DIGITS = 10
SPECIAL = 32 

# Brute force speed (attempts per second)
ATTACK_SPEED = 10**11

def get_charset(password):
    """Returns the character set size based on the password composition."""
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += LOWERCASE
    if re.search(r'[A-Z]', password): charset_size += UPPERCASE
    if re.search(r'[0-9]', password): charset_size += DIGITS
    if re.search(r'[\W_]', password): charset_size += SPECIAL
    return charset_size

def calculate_entropy(password):
    """Calculate entropy based on the password length and character set size."""
    charset_size = get_charset(password)
    if charset_size == 0:
        return 0
    return math.log2(charset_size) * len(password)

def estimate_bruteforce_time(password):
    """Estimate the time it would take to brute force the password."""
    charset_size = get_charset(password)
    combinations = charset_size ** len(password)
    time_seconds = combinations / ATTACK_SPEED
    return time_seconds

def format_time(seconds):
    """Format time in seconds into a readable format (years, days, hours, minutes)."""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"

def check_password_strength(password):
    """Check the password strength based on entropy and brute force estimates."""
    entropy = calculate_entropy(password)
    brute_force_time = estimate_bruteforce_time(password)
    
    if entropy < 40:
        strength = "❌ WEAK"
    elif entropy < 60:
        strength = "⚠️ ACCEPTABLE"
    else:
        strength = "✅ STRONG"
    
    return entropy, brute_force_time, strength

# Progress Bar Simulation
def display_progress_bar(password):
    """Show the progress of password evaluation with a progress bar."""
    print("\nEvaluating password strength...\n")
    for _ in tqdm(range(100), desc="Strength Evaluation", ncols=100):
        time.sleep(0.02)  # Simulate calculation time

def main():
    password = input("Enter your password: ")
    
    # Display progress bar while calculating
    display_progress_bar(password)

    # Calculate password strength
    entropy, brute_force_time, strength = check_password_strength(password)
    
    # Print results
    print(f"\nPassword Strength Evaluation:")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Estimated Brute-Force Time: {format_time(brute_force_time)}")
    print(f"Strength: {strength}")

# Run the program
if __name__ == "__main__":
    main()
