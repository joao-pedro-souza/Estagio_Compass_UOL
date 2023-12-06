class Aviao:

    def __init__(self, modelo, velocidade_maxima, capacidade, cor='Azul'):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor


aviao1 = Aviao('BOIENG456', '1500 km/h', 400)
aviao2 = Aviao('Embraer Praetor 600', '863 km/h', 14)
aviao3 = Aviao('Antonov An-2', '258 km/h', 12)

lista_avioes = [aviao1, aviao2, aviao3]

for aviao in lista_avioes:
    print(f'O avião de modelo "{aviao.modelo}" possui velocidade máxima de "{aviao.velocidade_maxima}", capacidade para "{aviao.capacidade}" passageiros: Cor {aviao.cor}')