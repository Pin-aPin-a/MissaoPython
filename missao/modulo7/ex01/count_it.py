#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if len(sys.argv)<1 :
    print("none")

else:
    print (f"Parameters: {len(sys.argv)}")
    for parametro in sys.argv :
        print (f"{parametro} : {len(parametro)}")
