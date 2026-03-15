def vigenere_sq(alphabet):
    square = []

    # Build square as list of lists
    for i in range(len(alphabet)):
        row = []
        for j in range(len(alphabet)):
            row.append(alphabet[(i + j) % len(alphabet)])
        square.append(row)

    # Print header
    print("|   | " + " | ".join(alphabet) + " |")

    # Divider
    print("|---|" + "---|" * len(alphabet))

    # Print rows
    for i, row in enumerate(square):
        print(f"| {alphabet[i]} | " + " | ".join(row) + " |")

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plain_index = letter_to_index(plaintext_letter, alphabet)

    cipher_index = (key_index + plain_index) % len(alphabet)

    return index_to_letter(cipher_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []

    plaintext = plaintext.upper()
    key = key.upper()

    for i, letter in enumerate(plaintext):
        if letter in alphabet:
            key_letter = key[i % len(key)]
            cipher_letter = vigenere_index(key_letter, letter, alphabet)
            cipher_text.append(cipher_letter)

    return "".join(cipher_text)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)

    plain_index = (cipher_index - key_index) % len(alphabet)

    return index_to_letter(plain_index, alphabet)


def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = []

    cipher_text = cipher_text.upper()
    key = key.upper()

    for i, letter in enumerate(cipher_text):
        if letter in alphabet:
            key_letter = key[i % len(key)]
            plain_letter = undo_vigenere_index(key_letter, letter, alphabet)
            plain_text.append(plain_letter)

    return "".join(plain_text)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "DAVINCI"

encrypted_store = []


def menu_encrypt():
    plaintext = input("Enter plaintext: ")
    cipher = encrypt_vigenere(key, plaintext, alphabet)
    encrypted_store.append(cipher)
    print("Encrypted:", cipher)


def menu_decrypt():
    for text in encrypted_store:
        plain = decrypt_vigenere(key, text, alphabet)
        print("Decrypted:", plain)


def menu_dump():
    print("Encrypted List:")
    print(encrypted_store)


menu = [
    ["Encrypt", menu_encrypt],
    ["Decrypt", menu_decrypt],
    ["Dump Encrypted Text", menu_dump],
    ["Quit", None]
]


def run_app():
    while True:
        print("\nMenu")

        for i, item in enumerate(menu):
            print(f"{i+1}. {item[0]}")

        choice = int(input("Select option: "))

        if choice == 4:
            print("Goodbye!")
            break

        action = menu[choice-1][1]
        action()


run_app()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "DAVINCI"

encrypted_store = []


def menu_encrypt():
    plaintext = input("Enter plaintext: ")
    cipher = encrypt_vigenere(key, plaintext, alphabet)
    encrypted_store.append(cipher)
    print("Encrypted:", cipher)


def menu_decrypt():
    for text in encrypted_store:
        plain = decrypt_vigenere(key, text, alphabet)
        print("Decrypted:", plain)


def menu_dump():
    print("Encrypted List:")
    print(encrypted_store)


menu = [
    ["Encrypt", menu_encrypt],
    ["Decrypt", menu_decrypt],
    ["Dump Encrypted Text", menu_dump],
    ["Quit", None]
]


def run_app():
    while True:
        print("\nMenu")

        for i, item in enumerate(menu):
            print(f"{i+1}. {item[0]}")

        choice = int(input("Select option: "))

        if choice == 4:
            print("Goodbye!")
            break

        action = menu[choice-1][1]
        action()


run_app()
