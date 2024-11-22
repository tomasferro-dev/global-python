from typing import List, Tuple
import random


class Detector:
    """
    Clase Detector que verifica la presencia de mutantes en una matriz de ADN.
    """
    def __init__(self, atributo1: str, atributo2: str):
        """
        Inicializa el Detector con dos atributos.

        :param atributo1: Primer atributo descriptivo.
        :param atributo2: Segundo atributo descriptivo.
        """
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def detectar_mutantes(self, matriz_adn: List[str]) -> bool:
        """
        Detecta si hay mutantes en una matriz de ADN.

        :param matriz_adn: Lista de cadenas que representan la matriz de ADN.
        :return: True si se detecta un mutante, False en caso contrario.
        """
        matriz = self._convertir_matriz(matriz_adn)

        return any([
            self._verificar_horizontal(matriz),
            self._verificar_vertical(matriz),
            self._verificar_diagonal_izq_der(matriz),
            self._verificar_diagonal_der_izq(matriz)
        ])

    def _convertir_matriz(self, matriz_adn: List[str]) -> List[List[str]]:
        """
        Convierte la matriz de ADN en una lista de listas de caracteres.

        :param matriz_adn: Lista de cadenas de ADN.
        :return: Matriz convertida en lista de listas.
        """
        return [list(fila) for fila in matriz_adn]

    def _verificar_horizontal(self, matriz: List[List[str]]) -> bool:
        for fila in matriz:
            for i in range(len(fila) - 3):
                if fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return True
        return False

    def _verificar_vertical(self, matriz: List[List[str]]) -> bool:
        for col in range(len(matriz[0])):
            for fila in range(len(matriz) - 3):
                if matriz[fila][col] == matriz[fila + 1][col] == matriz[fila + 2][col] == matriz[fila + 3][col]:
                    return True
        return False

    def _verificar_diagonal_izq_der(self, matriz: List[List[str]]) -> bool:
        for fila in range(len(matriz) - 3):
            for col in range(len(matriz[0]) - 3):
                if matriz[fila][col] == matriz[fila + 1][col + 1] == matriz[fila + 2][col + 2] == matriz[fila + 3][col + 3]:
                    return True
        return False

    def _verificar_diagonal_der_izq(self, matriz: List[List[str]]) -> bool:
        for fila in range(len(matriz) - 3):
            for col in range(3, len(matriz[0])):
                if matriz[fila][col] == matriz[fila + 1][col - 1] == matriz[fila + 2][col - 2] == matriz[fila + 3][col - 3]:
                    return True
        return False


class Mutador:
    """
    Clase Mutador que define mutaciones en matrices de ADN.
    """
    def __init__(self, base_nitrogenada: str, matriz_adn: List[List[str]], atributo2: str):
        """
        Inicializa un Mutador con una base nitrogenada y una matriz de ADN.

        :param base_nitrogenada: Base nitrogenada que se usará en las mutaciones.
        :param matriz_adn: Matriz de ADN a modificar.
        :param atributo2: Otro atributo descriptivo.
        """
        self.base_nitrogenada = base_nitrogenada
        self.matriz_adn = matriz_adn
        self.atributo2 = atributo2

    def crear_mutante(self):
        """
        Método genérico para implementar mutaciones. Debe ser sobrescrito en clases hijas.
        """
        pass


class Radiacion(Mutador):
    """
    Clase Radiacion que implementa mutaciones horizontales y verticales.
    """
    def crear_mutante(self, base_nitrogenada: str, posicion_inicial: Tuple[int, int], orientacion_de_la_mutacion: str) -> List[List[str]]:
        """
        Crea un mutante en la matriz de ADN.

        :param base_nitrogenada: Base nitrogenada para la mutación.
        :param posicion_inicial: Posición inicial en la matriz (fila, columna).
        :param orientacion_de_la_mutacion: Orientación de la mutación ('H' para horizontal, 'V' para vertical).
        :return: Matriz de ADN mutada.
        """
        fila, columna = posicion_inicial

        if base_nitrogenada not in ["A", "T", "C", "G"]:
            raise ValueError("La base nitrogenada debe ser una de las siguientes: A, T, C, G")

        if orientacion_de_la_mutacion not in ["H", "V"]:
            raise ValueError("La orientación de la mutación debe ser 'H' o 'V'")

        try:
            if orientacion_de_la_mutacion == "H":
                if columna + 3 >= len(self.matriz_adn[0]):
                    raise IndexError("No hay suficientes columnas para la mutación horizontal")
                for i in range(4):
                    self.matriz_adn[fila][columna + i] = base_nitrogenada

            elif orientacion_de_la_mutacion == "V":
                if fila + 3 >= len(self.matriz_adn):
                    raise IndexError("No hay suficientes filas para la mutación vertical")
                for i in range(4):
                    self.matriz_adn[fila + i][columna] = base_nitrogenada

        except IndexError as e:
            print(f"Error: {e}")
            self._aplicar_mutacion_predeterminada(base_nitrogenada)

        return self.matriz_adn

    def _aplicar_mutacion_predeterminada(self, base_nitrogenada: str):
        """
        Aplica una mutación predeterminada en la matriz de ADN.

        :param base_nitrogenada: Base nitrogenada para la mutación.
        """
        posicion_inicial = (2, 2)
        for i in range(4):
            self.matriz_adn[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada


class Virus(Mutador):
    """
    Clase Virus que implementa mutaciones diagonales.
    """
    def crear_mutante(self, base_nitrogenada: str, posicion_inicial: Tuple[int, int]) -> List[List[str]]:
        """
        Crea un mutante diagonal en la matriz de ADN.

        :param base_nitrogenada: Base nitrogenada para la mutación.
        :param posicion_inicial: Posición inicial en la matriz (fila, columna).
        :return: Matriz de ADN mutada.
        """
        fila, columna = posicion_inicial

        if base_nitrogenada not in ["A", "T", "C", "G"]:
            raise ValueError("La base nitrogenada debe ser una de las siguientes: A, T, C, G")

        try:
            if self._puede_mutar_diagonal_derecha(fila, columna):
                self._mutar_diagonal_derecha(base_nitrogenada, fila, columna)
            elif self._puede_mutar_diagonal_izquierda(fila, columna):
                self._mutar_diagonal_izquierda(base_nitrogenada, fila, columna)
            else:
                raise IndexError("No hay suficientes elementos para completar la mutación diagonal")

        except IndexError as e:
            print(f"Error: {e}")

        return self.matriz_adn

    def _puede_mutar_diagonal_derecha(self, fila: int, columna: int) -> bool:
        return fila + 3 < len(self.matriz_adn) and columna + 3 < len(self.matriz_adn[0])

    def _mutar_diagonal_derecha(self, base_nitrogenada: str, fila: int, columna: int):
        for i in range(4):
            self.matriz_adn[fila + i][columna + i] = base_nitrogenada

    def _puede_mutar_diagonal_izquierda(self, fila: int, columna: int) -> bool:
        return fila + 3 < len(self.matriz_adn) and columna - 3 >= 0

    def _mutar_diagonal_izquierda(self, base_nitrogenada: str, fila: int, columna: int):
        for i in range(4):
            self.matriz_adn[fila + i][columna - i] = base_nitrogenada


class Sanador:
    """
    Clase Sanador que corrige mutantes en una matriz de ADN.
    """
    def __init__(self, atributo1: str, atributo2: str):
        """
        Inicializa el Sanador con dos atributos y un Detector.

        :param atributo1: Primer atributo descriptivo.
        :param atributo2: Segundo atributo descriptivo.
        """
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.detector = Detector(atributo1, atributo2)

    def sanar_mutantes(self, matriz_adn: List[str]) -> List[str]:
        """
        Corrige mutaciones en una matriz de ADN.

        :param matriz_adn: Matriz de ADN a verificar.
        :return: Matriz de ADN corregida.
        """
        if self.detector.detectar_mutantes(matriz_adn):
            nuevo_adn = self._generar_adn_aleatorio()
            while self.detector.detectar_mutantes(nuevo_adn):
                nuevo_adn = self._generar_adn_aleatorio()
            return nuevo_adn
        return matriz_adn

    def _generar_adn_aleatorio(self) -> List[str]:
        """
        Genera una matriz de ADN aleatoria.

        :return: Matriz de ADN aleatoria.
        """
        bases_nitrogenadas = ["A", "T", "C", "G"]
        return [''.join(random.choices(bases_nitrogenadas, k=6)) for _ in range(6)]
