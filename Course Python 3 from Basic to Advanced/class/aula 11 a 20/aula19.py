logged_user = False

if logged_user:
    msg = 'Usuário Logado'
else:
    msg = 'Precisa logar'
print(msg)


msg = 'Usuário Logado' if logged_user else 'Precisa logar'
print(msg)

idade = 18
maior_de_idade = 'Não é maior' if idade < 18 else 'É maior'
print(maior_de_idade)

idade = 18
maior_de_idade = (idade < 18)
msg = 'Não é maior' if maior_de_idade else 'É maior'
print(msg)