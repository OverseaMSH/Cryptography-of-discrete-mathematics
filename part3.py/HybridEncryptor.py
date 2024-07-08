from typing import List
from RSAHandler import RSAHandler
from AESHandler import AESHandler


class HybridEncryptor:
    def __init__(self, r: RSAHandler, a: AESHandler):
        self.rsa_handler = r
        self.aes_handler = a

    def encrypt(self, plain_text: List[bytes]) -> List[bytes]:
        try:
            secret_key = self.aes_handler.key
            encrypted_data = [self.aes_handler.encrypt(
                data) for data in plain_text]
            encrypted_secret_key = self.rsa_handler.encrypt(secret_key)
            cipher_text = [encrypted_secret_key] + encrypted_data
            return cipher_text
        except Exception as e:
            print(f"Encryption error: {str(e)}")
            return []

    def decrypt(self, cipher_text: List[bytes]) -> List[bytes]:
        try:
            if len(cipher_text) < 2:
                raise ValueError("Invalid cipher text format")
            encrypted_secret_key = cipher_text[0]
            secret_key = self.rsa_handler.decrypt(encrypted_secret_key)
            decrypted_data = [self.aes_handler.decrypt(
                data) for data in cipher_text[1:]]
            return decrypted_data
        except Exception as e:
            print(f"Decryption error: {str(e)}")
            return []


def get_user_input(prompt: str) -> str:
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nUser cancelled input.")
        return ""


def main():
    rsa_handler = RSAHandler()
    aes_handler = AESHandler()
    encryptor = HybridEncryptor(rsa_handler, aes_handler)

    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            message = get_user_input("Enter message to encrypt: ")
            if message:
                encrypted = encryptor.encrypt([message.encode()])
                if encrypted:
                    print(f"Encrypted message: {encrypted}")
            else:
                print("No message entered.")

        elif choice == "2":
            cipher_text = get_user_input(
                "Enter cipher text to decrypt (format: [encrypted_secret_key, encrypted_data]): ")
            try:
                # Convert input string to list of bytes
                cipher_text = eval(cipher_text)
                decrypted = encryptor.decrypt(cipher_text)
                if decrypted:
                    print(f"Decrypted message: {decrypted[0].decode()}")
            except Exception as e:
                print(f"Error: {str(e)}")
                continue

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
