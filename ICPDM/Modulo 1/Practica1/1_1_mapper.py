#!/usr/bin/env python3

import sys

equiv_cod_paises = {}
paises_bueno = []

for linea in sys.stdin:
    # Dividimos la línea
    div_linea = linea.strip().split(',')

    # Es del fichero de opiniones y tiene por opinión "bueno"
    if len(div_linea) == 3 and div_linea[1] == 'bueno':
        # Se añade el país
        print(div_linea[2])
        
    # Es del fichero de países y no es la primera línea (el nombre de las columnas)
    elif len(div_linea) == 2 and div_linea[0] != 'Name':
        # Se manda la equivalencia entre ficheros
        print(f"{div_linea[0]},{div_linea[1]}")
