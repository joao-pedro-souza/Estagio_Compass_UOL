class Lampada:
    
    def __init__(self, ligada):
        self.ligada = ligada
        
    def esta_ligada(self):
        return self.ligada
        
    def liga(self):
        if self.ligada is False:
            self.ligada = True
            
    def desliga(self):
        if self.ligada:
            self.ligada = False


lampada = Lampada(False)

lampada.liga()
print(f'A lâmpada está ligada? {lampada.esta_ligada()}')
lampada.desliga()
print(f'A lâmpada ainda está ligada? {lampada.esta_ligada()}')
