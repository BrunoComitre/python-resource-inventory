frase =  'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

usuario = str(input('Digite uma letra: '))

while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    contador +=1
    
print(nova_string)
