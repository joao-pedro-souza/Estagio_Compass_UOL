from functools import reduce

def calcula_saldo(lancamentos) -> float:
    
    lista_valores = list(map(lambda tupla: + tupla[0] if tupla[1] == 'C' else - tupla[0], lancamentos))
    
    return reduce(lambda x, y: x+y, lista_valores)
    
