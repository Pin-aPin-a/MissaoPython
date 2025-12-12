#!/usr/bin/env python3

import sys

quantidade= len(sys.argv)-1

if quantidade>=1 :
    
    final_argumento="ism"
    #argumento_find= sys.argv[1].find("final_argumento")
    contador_ism= sys.argv[1].count(final_argumento)
    for i in range (quantidade) :
        argumento_find= sys.argv[i].find(final_argumento)
        if argumento_find==-1 :
            contador_ism= sys.argv[i].count(final_argumento)
            print (f"{i}ism)")
        
else:
    print("none")