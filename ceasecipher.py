"""
Caesar Cipher Encryption Tool
-----------------------------
A Caesar cipher is one of the simplest encryption techniques. Each letter in
the text is replaced by a letter a fixed number of positions (the "shift" or
"key") down the alphabet.

Example (shift = 3):
    Plain text :  HELLO
    Cipher text:  KHOOR

Decryption simply shifts in the opposite direction.
"""


def shift_text(text, shift):
    """Shift every letter in `text` by `shift` positions.
    Non-letters (spaces, digits, punctuation) are left unchanged."""
    result = ""
    for ch in text:
        if ch.isupper():
            # ord('A') = 65 -> convert to 0-25, shift, wrap with % 26, convert back
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result


def encrypt(text, key):
    return shift_text(text, key)


def decrypt(text, key):
    return shift_text(text, -key)


def get_key():
    """Keep asking until the user enters a valid integer key."""
    while True:
        try:
            return int(input("Enter shift value (key): "))
        except ValueError:
            print("Invalid key! Please enter a whole number.")


def main():
    print("=" * 45)
    print("        CAESAR CIPHER ENCRYPTION TOOL")
    print("=" * 45)

    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt and then decrypt (demo)")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            text = input("Enter plain text: ")
            key = get_key()
            print("\n--- Result ---")
            print(f"Original text  : {text}")
            print(f"Shift (key)    : {key}")
            print(f"Encrypted text : {encrypt(text, key)}")

        elif choice == "2":
            text = input("Enter cipher text: ")
            key = get_key()
            print("\n--- Result ---")
            print(f"Cipher text    : {text}")
            print(f"Shift (key)    : {key}")
            print(f"Decrypted text : {decrypt(text, key)}")

        elif choice == "3":
            text = input("Enter plain text: ")
            key = get_key()
            encrypted = encrypt(text, key)
            decrypted = decrypt(encrypted, key)
            print("\n--- Result ---")
            print(f"Original text  : {text}")
            print(f"Shift (key)    : {key}")
            print(f"Encrypted text : {encrypted}")
            print(f"Decrypted text : {decrypted}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()