file = open('aula82.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print(file.readline(), end='')
print(file.read())
file.close() 

##########################################

with open('aula82.txt', 'w+') as file:
    file.write('Linha 4\n')
    
    file.seek(0)
    print(file.read())

##########################################

import os

os.remove('aula82.txt')

##########################################

import json

d1 = {
    'Pessoa 1': {
        'nome': 'João',
        'idade': 56,
    },
    'Pessoa 2': {
        'nome': 'Maria',
        'idade': 54,
    },
}
print(d1)

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('aula82.json', 'w+') as file:
    file.write(d1_json)
    
with open('aula82.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    
for key, value in d1_json.items():
    print(key)
    for key_one, key_two in value.items():
        print(key_one, key_two)

os.remove('aula82.json')
