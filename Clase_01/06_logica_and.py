# Para entrar al sistema, el usuario debe ser "Admin" Y tener la clave "1234". Crear variables para ambos datos y verifica si el acceso es True o False.

usuario = "Admin"
clave = "1234"
acceso = usuario == "Admin" and clave == "1234"

print(acceso)
