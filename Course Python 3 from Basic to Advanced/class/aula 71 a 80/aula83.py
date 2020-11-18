def fala_oi():
    print('Oi')
    
fala_oi()
variavel = fala_oi()

######################################

# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Bruno']
clientes1 = lista_de_clientes(['João', 'Maria', 'José'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Ana'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
