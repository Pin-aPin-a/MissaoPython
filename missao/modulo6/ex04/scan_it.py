#!/usr/bin/env python3

import sys

quantidade= len(sys.argv) -1

if quantidade ==2 :
    palavra_chave= sys.argv[1]
    texto= sys.argv[2]
    contador= texto.count(palavra_chave)
    print (contador)

else:
    print ("none")




