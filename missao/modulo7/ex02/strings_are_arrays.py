#!/usr/bin/env python3

import sys

nome_script= len(sys.argv)-1
#array_teste = ["nome_arquivo","zzzzzzzz"]
#nome_script = len(array_teste)-1

if nome_script!=1:
    print("none")
else:
    argumento=sys.argv[1]
    #argumento = array_teste[1]
    letra_chave="z"
    contador= argumento.count(letra_chave)
    if contador==0 :
        print("none")
    else:
        print(f"{letra_chave*contador}")
