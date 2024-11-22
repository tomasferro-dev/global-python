# global-python


### A continuación verás algunas secuencias para utilizar en la aplicación
### Simplemente deberás copiar una y pegarla al inciar la aplicación


                                    GCACTGGTTACGAGAGCGCAGGCCTCAGTAAAGGGT
                                    ACGTTATTAACTGAGTTAAAACTCTCCACTGGATGG
                                    GTGTGTCTGTATCCATAGAGGCCAATGTTCGGAGTT
                                    GTCACGCAGTGGGCCACTCCGGAGTCGTGGTGAATT
                                    CCCGGGTCGTTGTTGCACGAGTTCGAATGATAACCA
                                    CAGCGATAACTATCATTCGACTATCAACCCGTGCGC
                                    GCATCCGCAGACGATCGACTTCTTACAGCAGATGAC
                                    CTGGCGGGCTGTACATATAGCCGTATTCTGATATGC
                                    CGGCTGGGATTTGCCCAAGTAACCCAGCCGTTTTGA
                                    GCCGAACTCAGACGGTTTTTCTCTATAAGTCCGGAA
                                    GAAAACATTCACTTACACGTAGTCATCGTTTGTCCT
                                    AGTTATCTCTTGTCACTCACTCACGGGAATGCTTTT
                                    CATGCTGTAGCGCCTATAACAAAATCTAAACGCATA
                                    GAGTGGATGAGCCATGATGGCATGCACATACACACG
                                    ATGTGCATAACTTTCGCTCTTAAACTCGATATCACT 

 # Aplicación de Análisis de ADN

Esta aplicación permite a los usuarios ingresar una secuencia de ADN, detectar mutaciones, aplicar radiación, aplicar virus y sanar el ADN. La secuencia de ADN debe ser una cadena de 36 caracteres que solo contenga las bases nitrogenadas A, T, C y G.

## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio:
```sh
   git clone https://github.com/tomasferro-dev/global-python.git
   cd global-python
```
2. Instala las dependencias (si las hay):
```sh
    pip install -r requirements.txt
```

## Uso

Ejecuta el archivo ejecutable.py:
```sh
    python ejecutable.py
```

Sigue las instrucciones en la consola para ingresar una secuencia de ADN y navegar por las opciones del menú.

## Ejemplo de Uso

Ejecuta el archivo ejecutable.py:

python ejecutable.py

Ingresa una secuencia de ADN de 36 caracteres cuando se te solicite. Por ejemplo:


>> Por favor, ingrese una secuencia de ADN de 36 caracteres (A, T, C, G): ATGCATGCATGCATGCATGCATGCATGCAT

Selecciona una opción del menú:


>> Menú de opciones:
1. Ver si es mutante
2. Aplicar radiación
3. Aplicar virus
4. Sanar ADN
5. Salir
>> Seleccione una opción (1-5): 1
La aplicación mostrará si la secuencia de ADN es mutante o no:


¿Es mutante?: Si, es mutante

Puedes seleccionar otras opciones del menú para aplicar radiación, aplicar virus o sanar el ADN.

## Estructura del Proyecto

>detector.py: Implementación de la clase Detector.
>mutador.py: Implementación de la clase Mutador.
>radiacion.py: Implementación de la clase Radiacion.
>virus.py: Implementación de la clase Virus.
>sanador.py: Implementación de la clase Sanador.
>interactivo.py: Funciones para interactuar con el usuario.
>menu.py: Menú interactivo para la aplicación.
>ejecutable.py: Archivo principal para ejecutar la aplicación.


## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama para tu contribución:


git checkout -b feature/nueva-funcionalidad
Realiza tus cambios y haz un commit:

git commit -m "Añadir nueva funcionalidad"
Haz un push a tu rama:

git push origin feature/nueva-funcionalidad
Abre un Pull Request en el repositorio original.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de davidlpz_y_facultamigos@gmail.com.

 ¡Gracias por usar la aplicación de análisis de ADN!  

 ## Miembros del grupo realizador de esta aplicación
 Tomas Ferro
 Sabrina Moreira
 David Lopez
