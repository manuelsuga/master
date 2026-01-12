#!/usr/bin/env python3

import sys

# Conteo de países
conteo_valoraciones_paises = {}
equivalencia_paises = {}

for linea in sys.stdin:
    linea = linea.strip()

    # Se trata de una equivalencia entre países
    if ',' in linea:
        linea = linea.split(',')
        nombre_pais = linea[0]
        cod_pais = linea[1]

        equivalencia_paises[cod_pais] = nombre_pais
    
    # Se trata de un código de un país con una valoración "bueno"
    else:
        if linea not in conteo_valoraciones_paises:
            conteo_valoraciones_paises[linea] = 0
        conteo_valoraciones_paises[linea] += 1

# Sustituimos las claves por el nombre de los paises
conteo_valoraciones_paises = { 
    equivalencia_paises[cod_pais] : conteo for cod_pais, conteo in conteo_valoraciones_paises.items() 
}

# Recorremos buscando el país con mayor número de valoraciones
maximo = -1
paises_maximo = []
# Quitamos el orden alfabético por país
for pais in conteo_valoraciones_paises:
    if conteo_valoraciones_paises[pais] > maximo:
        maximo = conteo_valoraciones_paises[pais]
        paises_maximo = [pais]
    # Si es el mismo valor, se almacena
    elif conteo_valoraciones_paises[pais] == maximo:
        paises_maximo.append(pais)

# Ahora simplemente recorremos los países ordenados alfabéticamente
for pais_maximo in sorted(paises_maximo):
    print(f'{maximo}\t["{pais_maximo}"]')
