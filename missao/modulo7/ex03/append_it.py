#!/usr/bin/env python3

import sys

quantidade= len(sys.argv)-1

if quantidade>=1 :
    sys.argv.pop(0)
    final_argumento="ism"
    for i in range (quantidade) :
        argumento_find= sys.argv[i].find(final_argumento,len(sys.argv[i])-3,len(sys.argv[i]))
        if argumento_find==-1 :
            print (f"{sys.argv[i]}ism")
        
else:
    print("none")