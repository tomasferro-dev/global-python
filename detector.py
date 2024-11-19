class Detector:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def detectar_mutantes(self, matriz_adn):
        # Convertir la matriz de ADN en una lista de listas de caracteres
        matriz = [list(fila) for fila in matriz_adn]

        # Verificar secuencias horizontales
        for fila in matriz:
            for i in range(len(fila) - 3):
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    print("Mutante horizontal")
                    return True

        # Verificar secuencias verticales
        for col in range(len(matriz[0])):
            for fila in range(len(matriz) - 3):
                if matriz[fila][col] == matriz[fila+1][col] == matriz[fila+2][col] == matriz[fila+3][col]:
                    print("Mutante vertical")
                    return True

        # Verificar secuencias diagonales (de izquierda a derecha)
        for fila in range(len(matriz) - 3):
            for col in range(len(matriz[0]) - 3):
                if matriz[fila][col] == matriz[fila+1][col+1] == matriz[fila+2][col+2] == matriz[fila+3][col+3]:
                    print("Mutante diagonal de izquierda a derecha")
                    return True

        # Verificar secuencias diagonales (de derecha a izquierda)
        for fila in range(len(matriz) - 3):
            for col in range(3, len(matriz[0])):
                if matriz[fila][col] == matriz[fila+1][col-1] == matriz[fila+2][col-2] == matriz[fila+3][col-3]:
                    print("Mutante diagonal de derecha a izquierda")
                    return True

        # Si no se encontraron mutantes
        return False
