#!/usr/bin/env python3
a = 0 
while a <= 10:
    print(f"Table de {a} :",end=' ')
    b = 0
    while b <= 10:
        rslt = a * b
        b += 1
        print(rslt,end=' ')
        continue
    a += 1
    print('\b')     
        
