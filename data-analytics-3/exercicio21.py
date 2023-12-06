class Passaro:

    def __init__(self, nome):
        self.nome = nome
    
    def voar(self):
        print(f'{self.nome}\nVoando')
    
    def emitir_som(self):
        print(f'{self.nome} emitindo som...')
    

class Pato(Passaro):
    
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print(f'{self.nome} emitindo som...')
        print(f'Quack Quack')


class Pardal(Passaro):
    
    def __init__(self, nome):
        super().__init__(nome)

    def emitir_som(self):
        print(f'{self.nome} emitindo som...')
        print(f'Piu Piu')


pato = Pato('Pato')
pardal = Pardal('Pardal')

pato.voar()
pato.emitir_som()
pardal.voar()
pardal.emitir_som()
