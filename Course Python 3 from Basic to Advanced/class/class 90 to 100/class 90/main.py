from pessoa import Pessoa

pessoa_um = Pessoa('Bruno', 76)
pessoa_dois = Pessoa('Joao', 56)

pessoa_um.eating('Banana')
pessoa_um.eating('Banana')
pessoa_um.stop_eating()
pessoa_um.eating('Banana')
pessoa_um.stop_eating()
pessoa_um.stop_eating()

pessoa_dois.eating('Abacaxi')
pessoa_dois.speaking('POO')
pessoa_dois.stop_eating()
pessoa_dois.speaking('POO')
pessoa_dois.eating('Abacaxi')
pessoa_dois.stop_speaking()
pessoa_dois.speaking('POO')

print(pessoa_um.year)
print(pessoa_dois.year)
print(Pessoa.year)

print(pessoa_um.get_year_birthday())
print(pessoa_dois.get_year_birthday())
