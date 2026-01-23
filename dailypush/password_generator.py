import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate_password(self, length=12, use_uppercase=True, use_digits=True, use_symbols=True):
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")

        # Start with at least one character from each selected type
        password = []
        if use_uppercase:
            password.append(random.choice(self.uppercase))
        if use_digits:
            password.append(random.choice(self.digits))
        if use_symbols:
            password.append(random.choice(self.symbols))

        # Fill the rest of the password
        all_chars = self.lowercase
        if use_uppercase:
            all_chars += self.uppercase
        if use_digits:
            all_chars += self.digits
        if use_symbols:
            all_chars += self.symbols

        for _ in range(length - len(password)):
            password.append(random.choice(all_chars))

        # Shuffle to avoid predictable patterns
        random.shuffle(password)
        return ''.join(password)

    def generate_multiple(self, count=5, length=12, **kwargs):
        return [self.generate_password(length, **kwargs) for _ in range(count)]

def main():
    generator = PasswordGenerator()
    print("Welcome to the Advanced Password Generator!")
    print("Generating 5 strong passwords:")
    passwords = generator.generate_multiple(5, length=16, use_uppercase=True, use_digits=True, use_symbols=True)
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd}")

if __name__ == "__main__":
    main()
