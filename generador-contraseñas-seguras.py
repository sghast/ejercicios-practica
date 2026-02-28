import string
import random
punctuation = "!@#$%&"
universo = string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation

#en un sistema real se define la longitud de la contraseña
longitud = 8

#obligatorios: asegurar que se tenga al menos una letra, número y símbolo
obligatorios = []
mayuscula = random.choice(string.ascii_uppercase)
minuscula = random.choice(string.ascii_lowercase)
numero =  random.choice(string.digits)
simbolo = random.choice(punctuation)

#incluirlos en el arreglo de obligatorios
obligatorios = [mayuscula, minuscula, numero, simbolo]

password = ""

for i in range(longitud - 4):
    obligatorios.append(random.choice(universo))

random.shuffle(obligatorios)

for i in obligatorios:
    password += i

print("Tu contraseña es: " + password + "\nNO LA COMPARTAS")