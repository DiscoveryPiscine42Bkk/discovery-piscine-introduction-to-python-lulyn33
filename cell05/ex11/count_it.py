#!/usr/bin/env python3
import sys

parameter = sys.argv
print(f"parameters: {len(parameter) -1}")
for i in parameter[1:]:
    print(f"{i} : {len(i)}")