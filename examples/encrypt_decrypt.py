key = 1


def encrypt(message: str):
    encrypted_message = ''
    for char in message:
        encrypted_message += chr(ord(char) + key)

    return encrypted_message


def decrypt(message: str):
    decrypted_message = ''
    for char in message:
        decrypted_message += chr(ord(char) - key)

    return decrypted_message
