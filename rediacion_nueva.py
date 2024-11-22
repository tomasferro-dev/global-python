from mutador import Mutador

#importar colorama
from colorama import init, Fore, Back, Style

#antes de ejecutar, verificar si tenes instalado colorama en tu equipo
#instalar: pip install colorama
#verificar si ya esta instalado correctamente: pip show colorama

# Inicializa colorama
init(autoreset=True)

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn, atributo2):
        super().__init__(base_nitrogenada, matriz_adn, atributo2)

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        # Validar que la base nitrogenada sea una de las permitidas
        if base_nitrogenada not in ["A", "T", "C", "G"]:
            raise ValueError(Fore.LIGHTMAGENTA_EX +"La base nitrogenada debe ser una de las siguientes: A, T, C, G")

        # Validar que la orientación de la mutación sea "H" o "V"
        if orientacion_de_la_mutacion not in ["H", "V"]:
            raise ValueError(Fore.LIGHTMAGENTA_EX +"La orientación de la mutación debe ser 'H' para horizontal o 'V' para vertical")

        try:
            if orientacion_de_la_mutacion == "H":
                # Verificar si hay suficientes columnas para la mutación horizontal
                if posicion_inicial[1] + 3 >= len(self.matriz_adn[0]):
                    raise IndexError(Fore.LIGHTRED_EX +"No hay suficientes columnas para completar la mutación horizontal")
                # Mutación horizontal
                for i in range(4):
                    self.matriz_adn[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                # Verificar si hay suficientes filas para la mutación vertical
                if posicion_inicial[0] + 3 >= len(self.matriz_adn):
                    raise IndexError(Fore.LIGHTRED_EX +"No hay suficientes filas para completar la mutación vertical")
                # Mutación vertical
                for i in range(4):
                    self.matriz_adn[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada
        except IndexError as e:
            print(f"Error: {e}")
            # Usar valores predeterminados si la mutación solicitada es imposible
            posicion_inicial = (2, 2)
            orientacion_de_la_mutacion = "H"
            if orientacion_de_la_mutacion == "H":
                # Mutación horizontal con valores predeterminados
                for i in range(4):
                    self.matriz_adn[posicion_inicial[0]][posicion_inicial[1] + i] = base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                # Mutación vertical con valores predeterminados
                for i in range(4):
                    self.matriz_adn[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada

        return self.matriz_adn
