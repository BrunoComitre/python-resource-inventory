import re

teste_1 = 'tipo de dano: ( ) rachadura (x) rompimento ( ) amassado f (x) obstruido'

teste_2 = 'tipo de dano: ( ) rachadura (x) rompimento ( ) amassado f (x) obstruido tipo de dano: (x) rachadura ( ) rompimento (x) amassado f () obstruido'

teste_3 = 'outra coisa: ( ) rachadura (x) rompimento ( ) amassado f (x) obstruido'


def extract_content(text):
    message = ''

    match_lines = re.findall("tipo de dano:.*", text)

    for line in match_lines:
        message = ' '.join(re.findall('(\(x\) [\S]*)', line))
    return message


t1 = extract_content(teste_1)
print(t1)

t2 = extract_content(teste_2)
print(t2)

t3 = extract_content(teste_3)
print(t3)
