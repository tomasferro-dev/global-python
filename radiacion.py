# radiacion.py
from mutador import Mutador

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, atributo1, atributo2):
        super().__init__(base_nitrogenada, atributo1, atributo2)

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        # Validar que la base nitrogenada sea una de las permitidas
        if base_nitrogenada not in ["A", "T", "C", "G"]:
            raise ValueError("La base nitrogenada debe ser una de las siguientes: A, T, C, G")

        # Validar que la orientación de la mutación sea "H" o "V"
        if orientacion_de_la_mutacion not in ["H", "V"]:
            raise ValueError("La orientación de la mutación debe ser 'H' para horizontal o 'V' para vertical")

        # Crear una matriz de ADN de ejemplo (6x6)
        matriz_adn = [
            ["A", "T", "G", "C", "A", "T"],
            ["G", "A", "T", "C", "G", "A"],
            ["T", "G", "A", "C", "T", "G"],
            ["C", "G", "T", "A", "C", "G"],
            ["A", "T", "G", "C", "A", "T"],
            ["G", "A", "T", "C", "G", "A"]
        ]

        fila, columna = posicion_inicial

        try:
            if orientacion_de_la_mutacion == "H":
                # Verificar si hay suficientes columnas para la mutación horizontal
                if columna + 3 >= len(matriz_adn[0]):
                    raise IndexError("No hay suficientes columnas para completar la mutación horizontal")
                # Mutación horizontal
                for i in range(4):
                    matriz_adn[fila][columna + i] = base_nitrogenada
                print("La matriz con mutacion horizotal es: ")
            elif orientacion_de_la_mutacion == "V":
                # Verificar si hay suficientes filas para la mutación vertical
                if fila + 3 >= len(matriz_adn):
                    raise IndexError("No hay suficientes filas para completar la mutación vertical")
                # Mutación vertical
                for i in range(4):
                    matriz_adn[fila + i][columna] = base_nitrogenada
                print("La matriz con mutacion horizotal es: ")

        except IndexError as e:
            print(f"Error: {e}")
            print("La matriz vuelve a su estado inicial")
            # return matriz_adn

        return matriz_adn
