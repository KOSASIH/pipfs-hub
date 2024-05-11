from cryptography.fernet import Fernet

def encrypt_data(data, key):
    # Encrypt data using PyCrypto or cryptography

    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())

    return encrypted_data

def decrypt_data(encrypted_data, key):
    # Decrypt data using PyCrypto or cryptography

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()

    return decrypted_data
