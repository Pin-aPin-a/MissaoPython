#!/usr/bin/env python3

import sys


sys.argv.pop (0)

if len(sys.argv)<2 :
    print ("none")

else:
    argumentos_invertidos= sys.argv[::-1]
    for argumento in argumentos_invertidos: 
        print(argumento)
