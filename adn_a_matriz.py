def convertir_adn_a_matriz(secuencia_adn):
    if len(secuencia_adn) != 36:
        raise ValueError("La secuencia de ADN debe tener exactamente 36 caracteres.")

    # Dividir la cadena de 36 caracteres en 6 subcadenas de 6 caracteres cada una
    matriz_adn = [secuencia_adn[i:i+6] for i in range(0, 36, 6)]
    return matriz_adn