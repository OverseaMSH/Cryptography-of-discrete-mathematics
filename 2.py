import pyaes
import random

class KeyExchange:
    def __init__(self, private_key: int):
        self.private_key = private_key
        self.prime = None
        self.shared_secret = None
    
    def configure(self, parameters: tuple):
        self.prime, self.generator = parameters
    
    def compute_shared_secret(self, peer_public_key: int):
        self.shared_secret = pow(peer_public_key, self.private_key, self.prime)
        self.encryption_key = str(self.shared_secret).zfill(32).encode('utf-8')
    
    def encrypt(self, plaintext: str) -> bytes:
        aes = pyaes.AESModeOfOperationCTR(self.encryption_key)
        ciphertext = aes.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext: bytes) -> str:
        aes = pyaes.AESModeOfOperationCTR(self.encryption_key)
        decrypted_text = aes.decrypt(ciphertext)
        return decrypted_text.decode('utf-8')

if __name__ == "__main__":
    PRIME_NUMBER = 23
    GENERATOR = 5

    alice_private_key = random.randint(1, PRIME_NUMBER - 1)
    bob_private_key = random.randint(1, PRIME_NUMBER - 1)

    alice = KeyExchange(alice_private_key)
    bob = KeyExchange(bob_private_key)

    alice.configure((PRIME_NUMBER, GENERATOR))
    bob.configure((PRIME_NUMBER, GENERATOR))

    alice_public_key = pow(GENERATOR, alice_private_key, PRIME_NUMBER)
    bob_public_key = pow(GENERATOR, bob_private_key, PRIME_NUMBER)

    alice.compute_shared_secret(bob_public_key)
    bob.compute_shared_secret(alice_public_key)

    shared_key = alice.shared_secret
    
    encryption_key = str(shared_key).zfill(32).encode('utf-8')
    print(f"Encryption Key: {encryption_key}")

    test_message = "this is a test!"

    encrypted_message = alice.encrypt(test_message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = bob.decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
    print("Decryption successful:", decrypted_message == test_message)
