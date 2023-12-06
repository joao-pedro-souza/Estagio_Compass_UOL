def calcular_valor_maximo(operadores,operandos) -> float:
    lista_numeros = list(zip(operadores, operandos))
    
    def operacao(lista):
        if lista[0] == '+':
            return lista[1][0] + lista[1][1]
        elif lista[0] == '-':
            return lista[1][0] - lista[1][1]
        elif lista[0] == '*':
            return lista[1][0] * lista[1][1]
        elif lista[0] == '/':
            return lista[1][0] / lista[1][1]
        elif lista[0] == '%':
            return lista[1][0] % lista[1][1]
    
    resultados = list(map(operacao, lista_numeros))
    
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos))
