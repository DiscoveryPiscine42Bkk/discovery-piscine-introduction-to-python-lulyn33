#!/usr/bin/env python3

def array_of_names(names):
    new_lst = []
    for k,v in names.items():
        new_lst.append((k.capitalize()) + ' '+ v.capitalize())
    return new_lst

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
