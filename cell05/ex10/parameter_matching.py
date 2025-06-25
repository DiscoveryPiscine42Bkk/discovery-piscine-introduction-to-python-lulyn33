#!/usr/bin/env python3
import sys

if len(sys.argv) != 2 :
    print('none')
else:
    var = input("What was the parameter? ")
    word = sys.argv[1]
    if var == word:
        print("Good job!")
    else:
        print("Nope, sorry...")
