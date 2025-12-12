#!/usr/bin/env python3

import sys

parametro= len(sys.argv)-1

if parametro==2 :
    sys.argv.pop(0)
    argumento_1=sys.argv[0]
    argumento_2=sys.argv[1]
    if argumento_1<argumento_2 :
        array=[]
        for i in range(int(argumento_1),int(argumento_2)+1) :
            array.append(i)
    print(array)
        

else:
    print("none")