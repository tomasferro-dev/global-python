def obtener_adn_usuario():
    while True:
        adn = input("Por favor, ingrese una secuencia de ADN de 36 caracteres (A, T, C, G): ")
        if len(adn) == 36 and all(c in "ATCG" for c in adn):
            break
        else:
            print("La entrada no es válida. Asegúrese de ingresar exactamente 36 caracteres y que todos sean A, T, C o G.")

    # Dividir la cadena de 36 caracteres en 6 subcadenas de 6 caracteres cada una
    matriz_adn = [list(adn[i:i+6]) for i in range(0, 36, 6)]
    return matriz_adn