# TASK 3 - Password Generator

import secrets
import string

def build_charset(use_lower, use_upper, use_digits, use_symbols):
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        # a common set of symbols for passwords
        chars += "!@#$%^&*()-_=+[]{};:,.<>?/|"
    return chars

def get_boolean_input(prompt):
    answer = input(prompt + " (y/n): ").strip().lower()
    return answer == "y" or answer == "yes"

def generate_password(length, charset):
    # using secrets.choice for cryptographic randomness
    return ''.join(secrets.choice(charset) for _ in range(length))

def main():
    print("=== Simple Password Generator ===")
    # Get length
    while True:
        try:
            length = int(input("Enter desired password length (e.g. 8-32): ").strip())
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Choose complexity
    use_lower = get_boolean_input("Include lowercase letters?")
    use_upper = get_boolean_input("Include uppercase letters?")
    use_digits = get_boolean_input("Include digits (0-9)?")
    use_symbols = get_boolean_input("Include symbols (e.g. @,#,$)?")

    # Ensure at least one charset chosen
    charset = build_charset(use_lower, use_upper, use_digits, use_symbols)
    if not charset:
        print("You must choose at least one character type. Exiting.")
        return

    password = generate_password(length, charset)
    print("\nGenerated password:\n" + password)

if __name__ == "__main__":
    main()
