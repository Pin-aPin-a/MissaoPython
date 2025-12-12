#!/usr/bin/env python3

question: str
question = input( "What you gotta say? : ")
while True:
    if question == "STOP":
        break
    question = input ("I got that! Anything else? : ")

