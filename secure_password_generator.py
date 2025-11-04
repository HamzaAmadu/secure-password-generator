import random
import time

# Function to generate a secure password
def generate_password():
    # Define character sets
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    special = '!@#$%^&*()_+-='
    
    # Start with one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special)
    ]
    
    # Add random characters to reach 12 total
    all_chars = uppercase + lowercase + numbers + special
    for i in range(8):
        password.append(random.choice(all_chars))
    
    # Shuffle the characters
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Function to check password strength
def check_password(password):
    # Check minimum length
    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    
    # Check for required character types
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # Verify all character types are present
    if not (has_upper and has_lower and has_digit and has_special):
        return "Weak: Password needs uppercase, lowercase, numbers, and special characters."
    
    # Determine strength based on length
    if len(password) >= 16:
        return "Strong: Good password!"
    else:
        return "Moderate: Password is okay but could be longer."

# Function for multi-factor authentication with OTP
def mfa_otp():
    # Generate 6-digit OTP
    otp = str(random.randint(100000, 999999))
    print("Your OTP is:", otp, "(It will expire in 60 seconds)")
    
    # Record start time
    start_time = time.time()
    
    # Get user input
    user_input = input("Enter the OTP you received: ")
    
    # Check if OTP expired
    if time.time() - start_time > 60:
        print("OTP has expired. Please try again.")
        return False
    
    # Verify OTP match
    if user_input == otp:
        print("OTP verified successfully!")
        return True
    else:
        print("Incorrect OTP.")
        return False

# Main program function
def main():
    print("Password Manager Tool")
    
    # Main program loop
    while True:
        # Display menu options
        print("\nMenu (1-5):")
        print("1. Generate new password")
        print("2. Check password strength")
        print("3. Test MFA with OTP")
        print("4. Show Password Rules")
        print("5. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-5): ")
        
        # Process user choice
        if choice == '1':
            password = generate_password()
            print("Your new generated password is:", password)
        elif choice == '2':
            password = input("Enter the password you would like to check: ")
            result = check_password(password)
            print(result)
        elif choice == '3':
            print("Testing MFA with OTP...")
            mfa_otp()
        elif choice == '4':
            print("Password must be at least 12 characters and include:")
            print("- Uppercase letters")
            print("- Lowercase letters")
            print("- Numbers")
            print("- Special characters")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again (1-5).")

# Program entry point
if __name__ == "__main__":
    main()
