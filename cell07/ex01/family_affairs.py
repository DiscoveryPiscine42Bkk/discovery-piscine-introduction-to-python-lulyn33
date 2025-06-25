#!/usr/bin/env python3

def find_the_redheads(para):
    new_lst = []
    for k,v in para.items():
        if v == 'red':
            new_lst.append(k)
    return new_lst

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
