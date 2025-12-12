#!/usr/bin/env python3

insert = input ("Entrada: ")
for i in range(len(insert)):
    if(insert[i].isupper()):
        print(insert[i].lower(), end= "")
    else:
        print(insert[i].upper(), end= "")
