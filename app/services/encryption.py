# Encryption service
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_file(file):
    key = ENCRYPTION_KEY
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file.read())
    nonce = cipher.nonce
    return get_random_bytes(16) + nonce + ciphertext + tag


def decrypt_file(encrypted_file):
    key = ENCRYPTION_KEY
    nonce = encrypted_file[16:32]
    ciphertext = encrypted_file[32:-16]
    tag = encrypted_file[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
