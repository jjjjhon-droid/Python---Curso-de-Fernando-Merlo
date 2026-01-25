# Pide dos números al usuario (numero_1 y numero_2). Imprime cuál de los dos es el más grande o si son iguales.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if numero_1 > numero_2:
    print("El primer numero es mayor")
elif numero_1 < numero_2:
    print("El segundo numero es mayor")
else:
    print("Los numeros son iguales")


