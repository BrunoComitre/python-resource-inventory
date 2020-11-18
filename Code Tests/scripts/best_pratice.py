# Adote a pep8.org e type annotations


def sum_two_numbers(
    a: int, b: int
) -> int:  # sum_two_numbers é o padrão snake case (tudo minúsculo e com uso de underline)
    # acima além do nome do argumento a, b. Ela ganha o tipo do argumento int e o tipo de retonrno -> int
    "Retorna a soma de a e b."  # Usar docstring - esse texto antes da função explica o objetivo da função
    return a + b


results: Mapping[
    str, int
] = {  # Mapping mostrando o tipo da chave e o tipo do valor que o dicionário tem
    "result10": sum_two_numbers(5, 5),
    "result256": sum_two_numbers(250, 6),
}

#####################

# Tenha apenas um tipo de retorno (utilize Exceptions). E de preferência anote tipos


def get_user(username: srt) -> User:
    """Query user by its username.
    :param username: A str holding username
    :returns: User instance
    :raises: UserNotFoundError
    """
    users = User(username=username).select()
    if not users:
        raise UserNotFoundError(f"{username} does not exist.")
    return users.first()
