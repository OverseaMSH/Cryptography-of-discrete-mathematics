from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class AESHandler:
    def __init__(self):
        # ثابت کردن کلید و IV (vector initialization) برای ساده‌سازی (برای کاربرد واقعی توصیه نمی‌شود)
        self.key = b"This is a 32-byte key for AES encryption."
        self.iv = os.urandom(16)  # تولید IV تصادفی برای هر رمزنگاری

    def encrypt(self, data: bytes) -> bytes:
        # ایجاد یک شی AES cipher با حالت CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # رمزنگاری داده‌ها
        cipher_text = encryptor.update(data) + encryptor.finalize()
        return cipher_text

    def decrypt(self, cipher_text: bytes) -> bytes:
        # ایجاد یک شی AES cipher با حالت CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # رمزگشایی داده‌ها
        decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()
        return decrypted_data
