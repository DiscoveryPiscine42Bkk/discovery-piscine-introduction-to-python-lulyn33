#!/usr/bin/env python3
import sys

param = sys.argv

if len(param) > 1:
    for i in param[-1:0:-1]:
        print(i)
else:
    print('none')