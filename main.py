import random
import string


def generate_password(length):
    password = ''
    for _ in range(length):
        if length > 0:
            password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*')
    return password


    def generate_password(length):
        password = ''
        while True:
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            if any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
                break
        return password

print(generate_password(8))

