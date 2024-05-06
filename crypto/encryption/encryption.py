from cryptography.fernet import Fernet

class Encryption:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        """Encrypt data using the Fernet symmetric encryption scheme."""
        return self.cipher_suite.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        """Decrypt data using the Fernet symmetric encryption scheme."""
        return self.cipher_suite.decrypt(encrypted_data).decode()
