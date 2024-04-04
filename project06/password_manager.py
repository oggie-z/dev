import json, hashlib, getpass, os, pyperclip, sys
from cryptography.fernet import Fernet

# Function for Hashing the Master Password
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

# generate a secret key. This should be done only once as you'll see. 
def generate_key():
    return Fernet.generate_key()

# Initialize Fernet cipher with the provided key. 
def initialize_cipher(key):
    return Fernet(key)

# Function to encrypt a password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()

# Function to decrypt a password.
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypt_password.encode()).decode()

# Functioin to register you.
def register(username, master_password):
    # Encrypt the master password before storing it
    hashed_master_password = hash_password(master_password)
    user_data = {'username': username, 'master_password': hashed_master_password}
    file_name = 'user_data.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as file:
            json.dump(user_data, file)
            print("\n[+] Registration complete!!\n")

    else:
        with open(file_name, 'x') as file:
            json.dump(user_data, file)

# Function to log you in.
def login(username, entered_password):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_password(entered_password)
        if entered_password_hash == stored_password_hash and username == user_data.get('username'):
            print("\n[+] Login Successful..\n")
        else:
            print("\n[-] Invalid Login credentials. Please use the credentials you used to register.\n")
            sys.exit()
    except FileNotFoundError:
        print("\n[-] You have not saved any passwords!\n")

# Function to view saved websites 
def view_websites(): 
    try:
        with open('passwords.json', 'r') as data:
            view = json.load(data)
            print("\nWebsites you saved...\n")
            for x in view:
                print(x['website'])
            print('\n')
    except FileNotFoundError:
        print("\n[-] You have not saved any passwords!\n")

# Load or generate the encryption key.
key_filename = 'encryption_key.key'
if os.path.exists(key_filename):
    with open(key_filename, 'rb') as key_file:
        key_file.write(key)

cipher = initialize_cipher(key)

# Function to add (save password).
def add_password(website, password):
    # Check if passwords.json exists
    if not os.path.exists('passwords.json'):
        # If Passwords.json doesn't exist, initialize it with an empty list
        data = []
    else:
        # Load existing data from passwords.json
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            # Handle the case where passwords.json is empty or invalid JSON.
            data = []
    # Encrypt the password 
    encrypt_password = encrypt_password(cipher, password)
    # Create a dictionary to store the website and password
    password_entry = {'website':, 'password': encrypted_password}
    data.append(password_entry)
    # Save the updated list back to passwords.json
    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

    def get_password(websites):
        # Check if passwords.json exist
        if not os.path.exists('passwords.json'):
            return None
        # Load existing data from passwords.json
        try:
            with open('password.json', 'r') as file:
                data = json.load(file)
        except json,JSONDecodeError:
            data = []

        # Loop through all websites and check if the requested website exists