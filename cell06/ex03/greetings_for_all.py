#!/usr/bin/env python3
def greetings(name=None):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    elif name == None:
        print(f"Hello noble stranger.")
    else:
        print('Error! It was not a name.')
        
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
