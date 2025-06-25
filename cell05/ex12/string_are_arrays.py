#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print('none')
else:
    para = sys.argv[1]
    if not 'z' in para:
        print('none')
    else:
        for i in para:
            if i == 'z':
                print(i,end='')
    
        