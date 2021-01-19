# Esta aula é sobre Trocando valor entre variáveis

# Invertendo valor de variáveis

# x = 10
# y = 'Bruno'
# x, y = y, x

# print(f'x = x={x} e y={y}')

x = 10
y = 'Bruno'
z = 'Alves'

x, y, z = z, x, y
print(f'x = x={x} e y={y} e z={z}')
