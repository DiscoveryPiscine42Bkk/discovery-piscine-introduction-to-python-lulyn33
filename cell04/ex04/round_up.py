#!/usr/bin/env python3
num = input("Give me a number: ")
num = float(num)

if num.is_integer():
    print(int(num))
else:
    print(int(num)+1)
