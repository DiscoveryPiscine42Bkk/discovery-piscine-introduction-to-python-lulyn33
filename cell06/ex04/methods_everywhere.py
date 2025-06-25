#!/usr/bin/env python3
import sys

param = sys.argv

def shrink(arg):
    return(arg[0:8])

def enlarge(arg):
    n = len(arg)
    while n < 8:
            arg = arg + 'Z'
            n += 1
    return(arg)
    

if len(param) <= 1:
    print('none')
else:
    for i in param[1::]:
        if len(i) < 8:
            print(enlarge(i))
        else:
            print(shrink(i))