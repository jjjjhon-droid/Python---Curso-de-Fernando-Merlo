# Instrucción: Pide al usuario su nota (0-100) y conviértela en letra:
# 90-100: Nota A
# 80-89: Nota B
# 70-79: Nota C
# > 70: Nota F

nota = int(input("Ingrese su nota: "))
letra = str

if nota >= 90 and nota <= 100:
    letra = "A"
elif nota >= 80 and nota < 90:
    letra = "B"
elif nota >= 70 and nota < 80:
    letra = "C"
else:
    letra = "F"

print("Su nota es: " + letra)
