"""
PEP = Python Enhancement Proposals | Propostas de aprimoramento python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.
"""


# [1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


# [2] - Utilize nomes em minúsculo, separados por underline
# para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


# [3] - Utilize 4 espaços para identação!
# tab pode ter espaço diferente em computadores diferentes(cuidado), use espaço
# e não misture tabs com espaço

if 'a' in 'banana':
    print('tem')


# [4] - Linhas em branco
# Separar funções e definições de classe com duas linhas em branco;
# Métodos dentro de uma classe devem ser separados com uma linha em branco;


# [5] - Imports
# Imports devem ser sempre feitos em linhas separadas;

# Import Errado
import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from time import clock_gettime , clock_settime

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from time import (
    clock_gettime_ns,
    clock_settime_ns,
    localtime,
    sleep
)

# Imports devem ser colocados no topo do arquivo,
# logo depois de quaisquer comentários ou dockstrings e
# antes de quaisquer constantes ou variáveis globais.


# [6] - Espaços em expressões e instruções

"""
# Não faça:
funcao( algo[ 1 ], { outro: 2 } ):
    pass

# Faça:

funcao(algo[1], {outro: 2})
"""


"""
# Não faça:
algo (1)

# Faça:
algo(1)
"""


"""
#Não faça
dict ['chave'] = lista [indice]

# Faça:
dict['chave'] = lista[indice]
"""


"""
# Não faça:
x              = 1
y              = 3
variavel_longa = 5

# Faça:
x = 1
y = 3
variavel_longa = 5
"""

# [7] - Termine sempre uma instrução com uma nova linha
