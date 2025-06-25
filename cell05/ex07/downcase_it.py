#!/usr/bin/env python3
import sys

param = sys.argv

if len(param) <= 1:
    print('none')
else:
    print((' '.join(param[1::])).lower())