# El precio de una entrada es 50. Pregunta al usuario: "¿Tienes tarjeta VIP? (si/no)".
#  Si responde "si", aplica un descuento del 50%. Al final imprime el precio a pagar.

entrada = 50
vip = input("Tienes tarjeta VIP? (si/no)")

if vip == "si":
    entrada = entrada * 0.5 

# entiendo que aca no es necesario el else, ya que si no se cumple la condicion, el precio sigue siendo el mismo

print(f"El precio a pagar es: {entrada}")