def encrypt(text, key):
    encrypted_text = ''
    for char in text:
        encrypted_text += chr((ord(char) + key) % 128)
    return encrypted_text

def decrypt(encrypted_text, key):
    decryped_text = ''
    for char in encrypted_text:
        decryped_text += chr((ord(char) - key) % 128)
    return decryped_text

massage = 'Hello, Word!'
encryption_key = 3
encrypted_message = encrypt(message, encryption_key)
print('Encrypted Message:', encrypted_message)
print('Decrypted Message:', decrypt(encrypt(encrypted_message, encryption_key)))