from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class AESHandler:
    def __init__(self):
        self.key = b"This is a 32-byte key for AES encryption."
        self.iv = os.urandom(16)  

    def encrypt(self, data: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()

        cipher_text = encryptor.update(data) + encryptor.finalize()
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()
        return decrypted_data
from AESHandler import AESHandler

def main():
    aes_handler = AESHandler()

    plaintext = b"Hello, World! This is a simple message."

    encrypted_text = aes_handler.encrypt(plaintext)
    print(f"Encrypted text (hex format): {encrypted_text.hex()}")

    decrypted_text = aes_handler.decrypt(encrypted_text)
    print(f"Decrypted text: {decrypted_text.decode()}")

if __name__ == "__main__":
    main()
