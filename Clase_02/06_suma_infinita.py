# Crea un programa que pida números al usuario continuamente y los vaya sumando. 
# El programa se detiene solamente cuando el usuario escribe el número 0. Al final, muestra la suma total.

numero = int(input("Ingrese un número: "))
suma = 0

while numero != 0:
    suma += numero # suma = suma + numero
    numero = int(input("Ingrese un número: "))

print("La suma total es:", suma)