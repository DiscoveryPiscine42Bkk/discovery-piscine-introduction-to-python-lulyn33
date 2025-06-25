#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for i in original_array:
    i = i + 2
    if i >= 10:
        new_array.append(i)

new_array = set(new_array)
        
print(f"{original_array}")
print(f"{new_array}")
