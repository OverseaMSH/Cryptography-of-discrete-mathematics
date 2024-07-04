from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
import os

class AESHandler:
    def __init__(self, key_size=256):

        self.key = os.urandom(key_size // 8)
        self.iv = os.urandom(16)

    def encrypt(self, data: bytes) -> bytes:
        padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        

        cipher_text = encryptor.update(padded_data) + encryptor.finalize()
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(cipher_text) + decryptor.finalize()
        
        unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
        plain_text = unpadder.update(padded_data) + unpadder.finalize()
        return plain_text
