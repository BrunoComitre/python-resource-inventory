"""
cout - itertools
"""

from itertools import count

contador = count()

contador = count(start=5)

contador = count(start=2, step=3)

contador = count(start=5, step=1.5)

contador = count(start=9, step=-1)

for valor in contador:
    print(valor)
    
    if valor >= 10 or valor <= -10:
        break
