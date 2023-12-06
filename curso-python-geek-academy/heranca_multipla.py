"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

#OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direita;
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


#OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes.
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'
    

class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'
        
        
class Pinguim(Aquatico, Terrestre):
    
    def __init__(self, nome):
        super().__init__(nome)


# Testando

tubarao = Aquatico('Tubas')
print(tubarao.nadar())
print(tubarao.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

pingu = Pinguim('Pingu')
print(pingu.andar())
print(pingu.nadar())
print(pingu.cumprimentar()) # Eu sou Pingu da terra! / Eu sou Pingu do mar!  ???? Method Resolution Order - MRO


# Objeto é instância de...

print(f'Pingu é instância de Pinguim {isinstance(pingu, Pinguim)}') # True
print(f'Pingu é instância de Aquatico {isinstance(pingu, Aquatico)}') # True
print(f'Pingu é instância de Terrestre {isinstance(pingu, Terrestre)}') # True
print(f'Pingu é instância de Animal {isinstance(pingu, Animal)}') # True
print(f'Pingu é instância de object {isinstance(pingu, object)}') # True
