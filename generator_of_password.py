import random

digitos = ["0", "1", "2", "3", "3", "4", "5", "6", "7", "8", "9",]
r = int(input("dime los dijitos que quieres en tu contraseña"))
password = ""
for i in range(r):
    password += random.choice(digitos)
print(password)
