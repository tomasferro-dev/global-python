# menu.py

from obtener_adn import obtener_adn_usuario, ingresar_matriz
from clases import Detector
from clases import Radiacion
from clases import Virus
from clases import Sanador
from clases import Mutador
from adn_a_matriz import convertir_adn_a_matriz
#importar colorama
from colorama import init, Fore, Back, Style

#antes de ejecutar, verificar si tenes instalado colorama en tu equipo
#instalar: pip install colorama
#verificar si ya esta instalado correctamente: pip show colorama

# Inicializa colorama
init(autoreset=True)


def mostrar_menu():
    print(Fore.BLUE +"\nMenú de opciones:")
    print(Fore.CYAN + "1. Ver si es mutante")
    print(Fore.CYAN +"2. Aplicar radiación")
    print(Fore.CYAN +"3. Aplicar virus")
    print(Fore.CYAN +"4. Sanar ADN")
    print(Fore.CYAN +"5. Salir")
    
def obtener_posicion_inicial():
    while True:
        try:
            fila = int(input(Fore.LIGHTGREEN_EX +"Ingrese la fila (0-5): "))
            columna = int(input(Fore.LIGHTGREEN_EX +"Ingrese la columna (0-5): "))
            if 0 <= fila < 6 and 0 <= columna < 6:
                return (fila, columna)
            else:
                print(Fore.LIGHTRED_EX +"La fila y la columna deben estar en el rango de 0 a 5.")
        except ValueError:
            print(Fore.LIGHTRED_EX +"Por favor, ingrese números válidos.")

def obtener_orientacion():
    while True:
        orientacion = input(Fore.LIGHTGREEN_EX +"Ingrese la orientación (H para horizontal, V para vertical): ").upper()
        if orientacion in ["H", "V"]:
            return orientacion
        else:
            print(Fore.LIGHTRED_EX +"La orientación debe ser 'H' para horizontal o 'V' para vertical.")

def obtener_base_nitrogenada():
    while True:
        base = input(Fore.MAGENTA +"Ingrese la base nitrogenada para la mutación (A, C, G, T): ").upper()
        if base in ["A", "C", "G", "T"]:
            return base
        else:
            print(Fore.LIGHTRED_EX +"La base nitrogenada debe ser una de las siguientes: A, C, G, T.")
            
def main():
    while True:
        matriz_adn = obtener_adn_usuario()
        # matriz_adn = ingresar_matriz()
        print(Fore.GREEN +"Matriz de ADN ingresada:")
        for fila in matriz_adn:
            print(fila)

        # try:
        #     matriz_adn = convertir_adn_a_matriz(matriz_adn)
        #     print(Fore.GREEN +"Matriz de ADN:")
        #     for fila in matriz_adn:
        #         print(fila)
        # except ValueError as e:
        #     print(f"Error: {e}")
        
        detector = Detector()
        radiacion = Radiacion("A", matriz_adn, "atributo2")
        virus = Virus("A", matriz_adn, "atributo2")
        sanador = Sanador()

        while True:
            mostrar_menu()
            opcion = input(Fore.BLUE +"Seleccione una opción (1-5): ")

            if opcion == "1":
                es_mutante = detector.detectar_mutantes(matriz_adn)
                mensaje_es_mutante = lambda: "Si, es mutante" if (es_mutante) else "No, no es mutante";
                print(f"¿Es mutante?: {mensaje_es_mutante()}")
            elif opcion == "2":
                base_nitrogenada = obtener_base_nitrogenada()
                posicion_inicial = obtener_posicion_inicial()
                orientacion = obtener_orientacion()
                matriz_adn = radiacion.crear_mutante(base_nitrogenada, posicion_inicial, orientacion)
                print(Fore.LIGHTMAGENTA_EX +"ADN después de aplicar radiación:")
                for fila in matriz_adn:
                    print(fila)
            elif opcion == "3":
                base_nitrogenada = obtener_base_nitrogenada()
                posicion_inicial = obtener_posicion_inicial()
                matriz_adn = virus.crear_mutante(base_nitrogenada, posicion_inicial)
                print(Fore.LIGHTYELLOW_EX +"ADN después de aplicar virus:")
                for fila in matriz_adn:
                    print(fila)
            elif opcion == "4":
                matriz_adn = sanador.sanar_mutantes(matriz_adn)
                print(Fore.LIGHTGREEN_EX +"ADN después de sanar:")
                for fila in matriz_adn:
                    print(fila)
            elif opcion == "5":
                break
            else:
                print(Fore.LIGHTRED_EX +"Opción no válida. Por favor, seleccione una opción válida.")

        reiniciar = input(Fore.LIGHTBLUE_EX +"¿Desea iniciar con otro ADN? (s/n): ")
        if reiniciar.lower() != "s":
            break

if __name__ == "__main__":
    main()
