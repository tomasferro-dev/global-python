import random

def generar_secuencia_adn(longitud=36):
    bases_nitrogenadas = ["A", "T", "C", "G"]
    secuencia = ''.join(random.choices(bases_nitrogenadas, k=longitud))
    return secuencia

def main():
    num_secuencias = int(input("¿Cuántas secuencias de ADN desea generar? "))
    secuencias = [generar_secuencia_adn() for _ in range(num_secuencias)]

    print("Secuencias de ADN generadas:")
    for secuencia in secuencias:
        print(secuencia)

if __name__ == "__main__":
    main()