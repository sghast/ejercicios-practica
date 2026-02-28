import string
import random
punctuation = "!@#$%&"
universo = string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation

#se pide la longitud de la contraseña solo por práctica, en un sistema real el usuario no ingresa la longitud
while True:
    longitud = int(input("Ingrese la longitud de su contraseña: "))
    if longitud >= 4: break
    else:
        print("La longitud debe ser al menos 4")

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

print(password)