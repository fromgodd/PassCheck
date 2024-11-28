import math
import os
import time
import string

# Load common passwords from file
def load_common_passwords(file_path="common.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return set(line.strip() for line in f)
    return set()

# Calculate password entropy
def calculate_entropy(password):
    if not password:
        return 0
    pool_size = 0
    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(char in string.punctuation for char in password):
        pool_size += len(string.punctuation)
    if any(char.isspace() for char in password):
        pool_size += 1
    return len(password) * math.log2(pool_size) if pool_size > 0 else 0

# Estimate brute-force time
def estimate_bruteforce_time(password, entropy):
    attempts_per_second = 1e9  # Assume 1 billion attempts/second
    total_combinations = 2 ** entropy
    time_seconds = total_combinations / attempts_per_second
    return time_seconds

# Format brute-force time into human-readable format
def format_time(seconds):
    intervals = [
        ('years', 60 * 60 * 24 * 365),
        ('days', 60 * 60 * 24),
        ('hours', 60 * 60),
        ('minutes', 60),
        ('seconds', 1),
    ]
    result = []
    for name, count in intervals:
        value = seconds // count
        if value > 0:
            result.append(f"{int(value)} {name}")
        seconds %= count
    return ", ".join(result) if result else "0 seconds"

# Determine strength level
def determine_strength(password, entropy, common_passwords):
    if password in common_passwords:
        return "WEAK", "🔴"
    if entropy < 28:
        return "WEAK", "🔴"
    elif entropy < 50:
        return "ACCEPTABLE", "🟡"
    elif entropy >= 50:
        return "STRONG", "🟢"
    return "UNKNOWN", "⚪"

# Main password checker
def check_password(password, common_passwords):
    entropy = calculate_entropy(password)
    brute_force_time = estimate_bruteforce_time(password, entropy)
    strength, emoji = determine_strength(password, entropy, common_passwords)

    print("\nPassword Analysis:")
    print(f"- Password: {'*' * len(password)}")
    print(f"- Entropy: {entropy:.2f} bits")
    # print(f"- Estimated Brute-force Time: {format_time(brute_force_time)}")
    print(f"- Strength: {emoji} {strength}")

# CLI interface
def main():
    print("Password Strength Checker")
    print("=========================")
    common_passwords = load_common_passwords()
    while True:
        password = input("\nEnter a password to check (or 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Goodbye!")
            break
        check_password(password, common_passwords)

if __name__ == "__main__":
    main()
