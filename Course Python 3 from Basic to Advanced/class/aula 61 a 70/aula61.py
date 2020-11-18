string = '012345678901234567890123456789012345678901234567890123456789'

n = 10
exercicio1 = [string[i:i + n] for i in range(0, len(string), n)]
print(exercicio1)

exercicio2 = '.'.join(exercicio1)
print(exercicio2)
