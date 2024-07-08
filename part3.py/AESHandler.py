from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


class AESHandler:
    def __init__(self, key: bytes = None):
        if key is None:
            self.key = os.urandom(32)  # Generate a 256-bit (32-byte) key
        else:
            self.key = key
        # Generate a random initialization vector (IV)
        self.iv = os.urandom(16)

    def encrypt(self, data: bytes) -> bytes:
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(
            self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(padded_data) + encryptor.finalize()
        return self.iv + cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        iv = cipher_text[:16]
        cipher_text = cipher_text[16:]

        cipher = Cipher(algorithms.AES(self.key),
                        modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(cipher_text) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        return data
