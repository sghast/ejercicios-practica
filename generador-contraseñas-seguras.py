import string
import random
punctuation = "!@#$%&"
universo = string.ascii_letters + string.digits + punctuation
password = ""

for i in range(8):
    letra = random.choice(universo)
    password += letra

print(password)