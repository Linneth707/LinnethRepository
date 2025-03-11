def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


matriz = [
    [3, 2, 1],
    [9, 7, 5],
    [6, 4, 8]
]

print("Matriz original:")
for fila in matriz:
    print(fila)


fila_a_ordenar = int(input("Ingresa el número de fila que deseas ordenar (0, 1 o 2): "))


if 0 <= fila_a_ordenar < len(matriz):
    bubble_sort(matriz[fila_a_ordenar])
else:
    print("Número de fila fuera de rango.")

print("\nMatriz después de ordenar la fila seleccionada:")
for fila in matriz:
    print(fila)
