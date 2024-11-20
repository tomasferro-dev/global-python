# virus.py
from mutador import Mutador

class Virus(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn, atributo2):
        super().__init__(base_nitrogenada, matriz_adn, atributo2)

    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        # Validar que la base nitrogenada sea una de las permitidas
        if base_nitrogenada not in ["A", "T", "C", "G"]:
            raise ValueError("La base nitrogenada debe ser una de las siguientes: A, T, C, G")

        # Crear una matriz de ADN de ejemplo (6x6)
        
        
        fila, columna = posicion_inicial

        try:
            # Intentar crear la mutación diagonal hacia abajo y a la derecha
            if self.puede_mutar_diagonal_derecha(self.matriz_adn, fila, columna):
                self.mutar_diagonal_derecha(self.matriz_adn, base_nitrogenada, fila, columna)
            elif self.puede_mutar_diagonal_izquierda(self.matriz_adn, fila, columna):
                # Intentar crear la mutación diagonal hacia abajo y a la izquierda
                self.mutar_diagonal_izquierda(self.matriz_adn, base_nitrogenada, fila, columna)
            else:
                raise IndexError("No hay suficientes elementos para completar ninguna mutación diagonal")

        except IndexError as e:
            print(f"Error: {e}")
            return self.matriz_adn

        return self.matriz_adn

    def puede_mutar_diagonal_derecha(self, matriz_adn, fila, columna):
        return fila + 3 < len(matriz_adn) and columna + 3 < len(matriz_adn[0])

    def mutar_diagonal_derecha(self, matriz_adn, base_nitrogenada, fila, columna):
        for i in range(4):
            matriz_adn[fila + i][columna + i] = base_nitrogenada

    def puede_mutar_diagonal_izquierda(self, matriz_adn, fila, columna):
        return fila + 3 < len(matriz_adn) and columna - 3 >= 0

    def mutar_diagonal_izquierda(self, matriz_adn, base_nitrogenada, fila, columna):
        for i in range(4):
            matriz_adn[fila + i][columna - i] = base_nitrogenada
