original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for i in original_array:
    i = i + 2
    if i >= 10:
        new_array.append(i)
        
print(f"{original_array}")
print(f"{new_array}")
