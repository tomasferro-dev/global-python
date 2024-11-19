from detector import Detector
from radiacion import Radiacion
from virus import Virus
from sanador import Sanador

def main():
    # Ejemplo de uso de las clases
    detector = Detector("atributo1", "atributo2")
    radiacion = Radiacion("A", "atributo1", "atributo2")
    # virus = Virus("T", "atributo1", "atributo2")
    # sanador = Sanador("atributo1", "atributo2")
    
    matriz_adn = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    mutante_horizontal = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
    mutante_diagonal = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]

    #********************************************************************
    # Ejemplo para detectar mutacion
    # es_mutante = detector.detectar_mutantes(mutante_vertical)
    # print(f"¿Es mutante?: {es_mutante}")
    #********************************************************************
    
    #********************************************************************
    # Ejemplo de radiacion
    # matriz_mutante_horizontal = radiacion.crear_mutante("T", (0, 0), "V")
    # for fila in matriz_mutante_horizontal:
    #     print("".join(fila))
    #********************************************************************
    
    #********************************************************************
    #Ejemplo de virus
    # virus = Virus("A", "atributo1", "atributo2")
    # matriz_mutante_diagonal_derecha = virus.crear_mutante("T", (0, 1))
    # for fila in matriz_mutante_diagonal_derecha:
    #     print("".join(fila))
    #********************************************************************

    #********************************************************************
    #Ejemplo de sanador
    sanador = Sanador("atributo1", "atributo2")
    matriz_adn_sanada = sanador.sanar_mutantes(mutante_horizontal)
    print("Matriz de ADN sanada:")
    for fila in matriz_adn_sanada:
        print(fila)



if __name__ == "__main__":
    main()