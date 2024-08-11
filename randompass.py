import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_punctuation=True):
    # Start with an empty string for characters
    characters = ''
    
    # Add letters to the character set if the user wants them
    if use_letters:
        characters += string.ascii_letters
    
    # Add digits to the character set if the user wants them
    if use_digits:
        characters += string.digits
    
    # Add punctuation to the character set if the user wants them
    if use_punctuation:
        characters += string.punctuation

    # Make sure there's at least one type of character to choose from
    if not characters:
        raise ValueError("At least one character type must be selected")

    # Generate the random password by picking random characters from the set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired password length: "))
        
        # Ask the user if they want to include letters in the password
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        
        # Ask the user if they want to include digits in the password
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        
        # Ask the user if they want to include punctuation in the password
        use_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'

        # Generate the password based on the user's preferences
        password = generate_password(length, use_letters, use_digits, use_punctuation)
        
        # Print the generated password
        print("Your random password is:", password)
    except ValueError as e:
        # Print an error message if something goes wrong
        print("Error:", e)

if __name__ == "__main__":
    main()
