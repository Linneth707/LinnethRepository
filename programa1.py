def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


valor_buscado = int(input("Ingresa el número que deseas buscar: "))


posicion = buscar_en_matriz(matriz, valor_buscado)


if posicion:
    print(f"El número {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El número {valor_buscado} no se encontró en la matriz.")
