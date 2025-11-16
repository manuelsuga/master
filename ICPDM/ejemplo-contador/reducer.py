#!/usr/bin/env python3
from collections import defaultdict
import sys
  
#ulizamos un diccionario para las palabras con un entero como valor
contador_palabras = defaultdict(int)

#por cada linea contamos el numero total de apariciones
for linea in sys.stdin:
    palabra, numero = linea.strip().split('\t')
    contador_palabras[palabra] += int(numero)

# escribimos por cada palabra el numero total de apariciones
for palabra in sorted(contador_palabras.keys()):
    print ('%s\t%s' % (contador_palabras[palabra], palabra))  
