# Define una contraseña secreta (ej: "1234"). 
# Pide la contraseña al usuario una y otra vez mientras no coincida con la secreta. 
# Cuando acierte, imprime "Acceso concedido".

contraseña = "1234"
contraseña_usuario = input("Ingrese la contraseña: ")

while contraseña_usuario != contraseña:
    contraseña_usuario = input("Incorrecto, vuelva a ingresar la contraseña: ")

print("Acceso concedido")

