# TUTORIAL DE : https://realpython.com/python-kwargs-and-args/

def concatenate(**kwargs: dict) -> int:
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# Tipo args, kwargs é apenas um nome, pode ser alterado para o que você quiser.
# Novamente, o que é importante aqui é o uso do operador de descompactação (**).


def concatenate_words(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate_words(a="Real", b="Python", c="Is", d="Great", e="!"))
