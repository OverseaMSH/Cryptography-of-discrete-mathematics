from typing import List, Tuple

class RSAHandler:
    def __init__(self, publicKey: Tuple[int, int], privateKey: Tuple[int, int]):
        self.publicKey = publicKey  # ذخیره کردن کلید عمومی (e, n)
        self.privateKey = privateKey  # ذخیره کردن کلید خصوصی (d, n)

    def encrypt(self, plainText: str) -> str:
        try:
            e, n = self.publicKey
            encryptedText = ""
            for char in plainText:
                encryptedChar = str((ord(char) ** e % n))
                encryptedText += encryptedChar + " "
            return encryptedText.strip()
        except Exception as error:
            print(f"Encryption failed: {error}")
            return ""

    def decrypt(self, cipherText: str) -> str:
        try:
            d, n = self.privateKey
            decryptedText = ""
            encryptedChars = cipherText.split()
            for encryptedChar in encryptedChars:
                decryptedChar = chr((int(encryptedChar) ** d % n))
                decryptedText += decryptedChar
            return decryptedText
        except Exception as error:
            print(f"Decryption failed: {error}")
            return ""

def gcd(a: int, b: int) -> int:
    try:
        while b:
            a, b = b, a % b
        return a
    except Exception as error:
        print(f"GCD calculation failed: {error}")
        return 1

def mod_inverse(e: int, phi: int) -> int:
    try:
        def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
            if a == 0:
                return b, 0, 1
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

        gcd, x, _ = extended_gcd(e, phi)
        if gcd != 1:
            raise Exception('معکوس ضریبی وجود ندارد')
        else:
            return x % phi
    except Exception as error:
        print(f"Modular inverse calculation failed: {error}")
        return 1

def generate_keys(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    try:
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        d = mod_inverse(e, phi)
        return (e, n), (d, n)
    except Exception as error:
        print(f"Key generation failed: {error}")
        return (0, 0), (0, 0)

# مثال تولید کلیدها و استفاده از کلاس RSAHandler
p = 61  # عدد اول کوچک برای سادگی
q = 53  # عدد اول کوچک برای سادگی
publicKey, privateKey = generate_keys(p, q)
rsaHandler = RSAHandler(publicKey, privateKey)

# گرفتن ورودی از کاربر و جلوگیری از ورود پیام خالی
while True:
    try:
        plainText = input("Enter your message: ")
        if plainText.strip():
            break
        else:
            print("Don't enter empty message!")
    except Exception as error:
        print(f"Error reading input: {error}")

while True:
    try:
        cipherText = rsaHandler.encrypt(plainText)
        if cipherText:
            print("Crypted text:", cipherText)
            decryptedText = rsaHandler.decrypt(cipherText)
            if decryptedText:
                print("Decrypted text:", decryptedText)
        else:
            print("Encryption failed, please try again.")
    except Exception as error:
        print(f"Error in encryption/decryption process: {error}")

    # سوال مجدد از کاربر برای ادامه
    while True:
        try:
            choice = input("Do you want to encrypt another message? (yes/no): ").strip().lower()
            if choice == 'yes':
                while True:
                    try:
                        plainText = input("Enter your message: ")
                        if plainText.strip():
                            break
                        else:
                            print("Don't enter empty message!")
                    except Exception as error:
                        print(f"Error reading input: {error}")
                break
            elif choice == 'no':
                print("Exiting the program.")
                exit(0)
            else:
                print("Please enter 'yes' or 'no'.")
        except Exception as error:
            print(f"Error reading choice: {error}")
