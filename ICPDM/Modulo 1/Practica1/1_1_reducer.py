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

# conteo_pais = {}
# for cod_pais in conteo_valoraciones_paises.keys():
#     conteo_pais[equivalencia_paises[cod_pais]] = conteo_valoraciones_paises[cod_pais]

# # Los mostramos ordenados alfabéticamente
for pais in sorted(conteo_valoraciones_paises):
    print(f'["{pais}"]\t{conteo_valoraciones_paises[pais]}')
