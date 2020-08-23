import string

def check_password_complexity(passwd: str):
    length = True if len(passwd) >= 8 else False
    lowercase = any([True if item in string.ascii_lowercase else False for item in passwd])
    uppercase = any([True if item in string.ascii_uppercase else False for item in passwd])
    digits = any([True if item in string.digits else False for item in passwd])
    whitespace = any([True if item in string.whitespace else False for item in passwd])
    return all([length, lowercase, uppercase, digits, whitespace])

print(check_password_complexity('AaBbCc10'))
print(check_password_complexity('sB8J akK0'))


'''
Nao pode menos de 8 numeros ou letras
Nao pode mais de 8 apenas numeros ou apenas letras maiusculas e minusculas
Nao pode nenhuma combinação com menos de 8 caracteres

Pode maior de 8 com letras maiusculas e minussculass e com caracteres especiaais
'''