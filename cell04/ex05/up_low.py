#!/usr/bin/env python3
word = input()
for i in word:
    if i == i.upper():
        i = i.lower()
        print(i,end='')
    else:
        if i == i.lower():
            i = i.upper()
            print(i,end='')
