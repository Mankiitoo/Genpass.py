import string
import random

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debe seleccionar al menos un tipo de carácter"

    random.seed()
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Obtener opciones del usuario
longitud = int(input("Ingrese el tamaño de la contraseña: "))
incluir_mayusculas = input("Incluir mayúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("Incluir minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

# Generar y mostrar la contraseña
contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
print("La contraseña generada es:", contraseña)
