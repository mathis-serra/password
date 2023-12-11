import string
import hashlib
import json

def hash_password(password):
    #Hash le mot de passe avec SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def save_passwords(passwords, filename='passwords.json'):
    # save passwords to JSON file
    with open(filename, 'w') as file:
        json.dump(passwords, file)

def load_passwords(filename='passwords.json'):
    try:
        # Load hash passwords from JSON file
        with open(filename, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = []
    return passwords

while True:
    password = input('Entrez un mot de passe : ')
    password_length = len(password)

    if password_length < 8:
        print('Le mot de passe est trop court')
    else:
        has_lowercase = any(c.islower() for c in password)
        has_uppercase = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)

        if has_lowercase and has_uppercase and has_digit and has_special:
            print('Le mot de passe est fort')
            
            # load passwords
            passwords = load_passwords()

            # add new password in json file
            passwords.append({'password': hashed_password})

            # save passwords 
            save_passwords(passwords)
            
            print('Mot de passe haché ajouté avec succès dans le fichier.')
            break
        else:
            print('Le mot de passe est trop faible. Veuillez réessayer.')

        

