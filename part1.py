from typing import List, Tuple

class RSAHandler:
    def __init__(self, publicKey: Tuple[int, int], privateKey: Tuple[int, int]):
        # ذخیره کردن کلید عمومی و خصوصی
        self.publicKey = publicKey  # (e, n)
        self.privateKey = privateKey  # (d, n)

    def encrypt(self, plainText: str) -> str:
        # رمزنگاری متن ساده با استفاده از کلید عمومی
        e, n = self.publicKey
        encryptedText = ""
        for char in plainText:
            # تبدیل کاراکتر به عدد صحیح، رمزنگاری و تبدیل به رشته قابل نمایش
            encryptedChar = str((ord(char) ** e % n))
            encryptedText += encryptedChar + " "  # اضافه کردن فاصله به عنوان جداکننده
        return encryptedText.strip()  # حذف فاصله اضافی انتهای رشته

    def decrypt(self, cipherText: str) -> str:
        # رمزگشایی متن رمز شده با استفاده از کلید خصوصی
        d, n = self.privateKey
        decryptedText = ""
        encryptedChars = cipherText.split()
        for encryptedChar in encryptedChars:
            # تبدیل رشته به عدد صحیح، رمزگشایی و تبدیل به کاراکتر
            decryptedChar = chr((int(encryptedChar) ** d % n))
            decryptedText += decryptedChar
        return decryptedText

# تابع برای محاسبه ب.م.م
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# تابع برای محاسبه معکوس ضریبی
def mod_inverse(e: int, phi: int) -> int:
    # استفاده از الگوریتم گسترده اقلیدس برای پیدا کردن معکوس ضریبی e به مد φ
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

# تابع برای تولید کلیدهای عمومی و خصوصی RSA
def generate_keys(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # انتخاب یک مقدار ثابت رایج برای e
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# مثال تولید کلیدها و استفاده از کلاس RSAHandler
p = 61  # عدد اول کوچک برای سادگی
q = 53  # عدد اول کوچک برای سادگی
publicKey, privateKey = generate_keys(p, q)
rsaHandler = RSAHandler(publicKey, privateKey)

# گرفتن ورودی از کاربر و جلوگیری از ورود پیام خالی
while True:
    plainText = input("Enter your message: ")
    if plainText.strip():
        break
    else:
        print("Don't enter empty message!")

# متن ساده برای رمزنگاری
cipherText = rsaHandler.encrypt(plainText)  # رمزنگاری متن ساده
decryptedText = rsaHandler.decrypt(cipherText)  # رمزگشایی متن رمز شده

print("Main text:", plainText)
print("Crypted text:", cipherText)
print("Decrypted text:", decryptedText)
