# sanador.py
import random
from detector import Detector

class Sanador:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.detector = Detector(atributo1, atributo2)

    def sanar_mutantes(self, matriz_adn):
        # Verificar si hay mutaciones en la matriz de ADN
        if self.detector.detectar_mutantes(matriz_adn):
            # Generar un nuevo ADN aleatoriamente hasta que no tenga mutaciones
            nuevo_adn = self.generar_adn_aleatorio()
            while self.detector.detectar_mutantes(nuevo_adn):
                nuevo_adn = self.generar_adn_aleatorio()
            return nuevo_adn
        else:
            return matriz_adn

    def generar_adn_aleatorio(self):
        bases_nitrogenadas = ["A", "T", "C", "G"]
        nuevo_adn = []
        for _ in range(6):
            fila = ''.join(random.choices(bases_nitrogenadas, k=6))
            nuevo_adn.append(fila)
        return nuevo_adn
