# Crea un programa que:
# 1 .Pida el total de la cuenta (puede tener decimales).
# 2 .Pida el porcentaje de propina que quieres dejar (ej. 10, 15, 20).
# 3 .Calcule cuánto es la propina y el nuevo total.
# 4 .Imprima un recibo detallado.

total_cuenta = float(input("Ingrese el total de la cuenta: "))
propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))
total_propina = total_cuenta * (propina / 100)
total_final = total_cuenta + total_propina

print("Recibo")
print("Total de la cuenta: ", total_cuenta)
print("Propina: ", propina)
print("Total con propina: ", total_final)


