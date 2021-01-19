# Esta aula é sobre índices e Fatiamento de strings

"""
Manipulando string - Aula 14
* String indices
* Fatiamento de strings [ínicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""

# Positivos        [0 1 2 3 4 5 6 7 8 9 10 11 12]
text_explanation = 'P y t h o n   C o u r  s  e'

text_explanation = 'P  y  t   h o n   C o u r s e'
# Negativos        [13 12 11 10 9 8 7 6 5 4 3 2 1]

text = 'Python Course'
print(text[2])
print(text[-1])

url = 'www.google.com.br/'
print(url[:-1])

new_string = text[2:6]
print(new_string)  # Exemplo de Fatiamento de string

new_string = text[0:6:2]  # Exemplo pulando caractere - vai do 0 ao 6 pulando de 2 em 2
print(new_string) 

print(len(text))
