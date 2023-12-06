class Pessoa:
    
    id = 0

    def __init__(self, nome):
        self.__nome = nome
        
        self.id = Pessoa.id + 1
        Pessoa.id += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    

pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
