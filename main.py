import sys
from algoritmoOtimo import *
from segundaChance import *
from conjuntoDeTrabalho import *

entrada = []

for linha in sys.stdin:
    linha = int(linha.replace('\n', ''))
    entrada.append(linha)

quadros = entrada[0]
entrada.pop(0)
paginas = entrada.copy()

# print(quadros)
# print(paginas)

print(segundaChance(paginas, quadros))
print(algoritmoOtimo(paginas, quadros))
print(conjuntoTrabalho(paginas, quadros))