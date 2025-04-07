# Escritura en archivo de texto

# Crea un nuevo archivo llamado my_notes.txt (modo 'w' para escribir)
with open('my_notes.txt', 'w') as file:
    # Escribe al menos tres líneas de notas personales
    file.write("Nota 1: Recordar estudiar para el examen de Física.\n")
    file.write("Nota 2: Comprar leche y pan en el supermercado.\n")
    file.write("Nota 3: Llamar a mamá más tarde.\n")

# Lectura del archivo de texto

# Abre el archivo para lectura (modo 'r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido del archivo línea por línea
    for line in file:
        # Muestra cada línea leída en la consola
        print(line.strip())  # strip() para eliminar los saltos de línea al final

# El archivo se cierra automáticamente al salir del bloque 'with'


