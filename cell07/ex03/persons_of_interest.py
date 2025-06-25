#!/usr/bin/env python3

def famous_births(para):
    sorted_list = sorted(para.items(), key=lambda item: int(item[1]["date_of_birth"]))
    for k,v in sorted_list:
        print(f"{v["name"]} is a great scientist born in {v['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
