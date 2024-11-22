from colorama import init, Fore, Back, Style

#antes de ejecutar, verificar si tenes instalado colorama en tu equipo
#instalar: pip install colorama
#verificar si ya esta instalado correctamente: pip show colorama

# Inicializa colorama
init(autoreset=True)



def obtener_adn_usuario():
    while True:
        adn = input(Fore.LIGHTCYAN_EX+"Por favor, ingrese una secuencia de ADN de 36 caracteres (A, T, C, G): "+ Style.RESET_ALL)
        if len(adn) == 36 and all(c in "ATCG" for c in adn):
            break
        else:
            print(Fore.LIGHTRED_EX +"La entrada no es válida. Asegúrese de ingresar exactamente 36 caracteres y que todos sean A, T, C o G."+ Style.RESET_ALL)

    # Dividir la cadena de 36 caracteres en 6 subcadenas de 6 caracteres cada una
    matriz_adn = [list(adn[i:i+6]) for i in range(0, 36, 6)]
    return matriz_adn



def ingresar_matriz() -> list[str]:
    """
    Permite al usuario ingresar una matriz de ADN de 6x6.

    :return: Lista de cadenas que representan la matriz de ADN.
    """
    print ( "Ingrese las filas de la matriz de ADN (6 cadenas de 6 caracteres, usando A, T, C, G):")
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"Fila {i + 1}: ").strip().upper()
            if len(fila) == 6 and all(base in "ATCG" for base in fila):
                matriz.append(fila)
                break
            else:
                print("\nError: La fila debe tener exactamente 6 caracteres y solo contener A, T, C o G.")
    return matriz