import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the possible character sets
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    # Ensure that the length is at least 1
    if length < 1:
        return "Error! Password length must be at least 1."

    # Generate the password by randomly choosing characters from the selected sets
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Prompt user to input desired password length
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Error! Please enter a valid number.")
        return
    
    # Ask user for complexity preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password8
    
    password = generate_password(length, use_uppercase, use_digits, use_special)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
