#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if len (sys.argv)!=1 :
    print ("none")

else:
    combinacao= sys.argv[0]
    entrada=input("What was the parameter? ")
    
    if entrada==combinacao :
        print("Good job!")
    else:
         print("Nope, sorry...")
