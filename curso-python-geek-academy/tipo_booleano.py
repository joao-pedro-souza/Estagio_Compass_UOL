"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> False

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True and True -> True
True and False -> True
False and True -> True
False and False -> False
"""
print(ativo or logado)

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
