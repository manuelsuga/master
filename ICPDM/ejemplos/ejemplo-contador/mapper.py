#!/usr/bin/env python3

import sys

# entrada estandar STDIN
for linea in sys.stdin:
  # eliminamos espacios
  linea = linea.strip()
  # dividimos cada linea en palabras
  palabras = linea.split()

  # cada palabra la escribimos junto con un 1 y esta es la entrada del reducer
  for palabra in palabras:
    print ('%s\t%s' % (palabra, 1))
