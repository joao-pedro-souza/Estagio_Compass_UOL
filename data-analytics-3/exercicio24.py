class Ordenadora:

    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    
    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        return self.listaBaguncada[::-1]
    

crescente = Ordenadora([3,4,2,1,5]).ordenacaoCrescente()
print(crescente)

decrescente = Ordenadora([9,7,6,8]).ordenacaoDecrescente()
print(decrescente)
