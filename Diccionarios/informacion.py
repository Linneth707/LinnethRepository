# Crear un diccionario con información personal ficticia.
informacion_personal = {
    "nombre": "Ana García",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

# Acceder y modificar el valor de "ciudad".
informacion_personal["ciudad"] = "Calderon"

# Agregar una nueva clave-valor para la profesión.
informacion_personal["profesion"] = "Desarrolladora de Software"

# Verificar si la clave "telefono" existe y agregarla si no existe.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad".
del informacion_personal["edad"]

# Imprimir el diccionario final.
print(informacion_personal)