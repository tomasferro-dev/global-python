from detector import Detector
from radiacion import Radiacion
from virus import Virus
from sanador import Sanador

def main():
    
    matriz_adn = ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    mutante_horizontal = ["TTTTCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
    mutante_vertical = ["AGATCA", "GATTCA", "CAATAT", "GAGTTA", "ATTGCG", "CTGTTC"]
    mutante_diagonal = ["TGATCA", "GTTTCA", "CATCAT", "GAGTTA", "ATTGCG", "CTGTTC"]

    #********************************************************************
    # Ejemplo para detectar mutacion
    detector = Detector("atributo1", "atributo2")
    es_mutante = detector.detectar_mutantes(matriz_adn)
    mensaje_es_mutante = lambda: "Si, es mutante" if (es_mutante) else "No, no es mutante";
    print(f"¿Es mutante?: {mensaje_es_mutante()}")
    #********************************************************************
    
    #********************************************************************
    # Ejemplo de radiacion
    # radiacion = Radiacion("A", "atributo1", "atributo2")
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
    # sanador = Sanador("atributo1", "atributo2")
    # matriz_adn_sanada = sanador.sanar_mutantes(mutante_horizontal)
    # print("Matriz de ADN sanada:")
    # for fila in matriz_adn_sanada:
    #     print(fila)



if __name__ == "__main__":
    main()