#!/usr/bin/env python3
import sys

param = sys.argv
def downcase_it(arg):
    return str(arg).lower()

if len(param) <= 1:
    print('none')
else:
    for i in param[1::]:
        print(downcase_it(i))
        