#!/usr/bin/env python3

number = 1
cont = 0
while cont <=10 :
    multiplicacao = number * cont
    print (f"Table of {multiplicacao}: ", end= "")
    numero = 0
    while numero <= 10 :
        calculo = cont * numero
        print (calculo, end= " ")
        numero +=1
    print()
    cont +=1
