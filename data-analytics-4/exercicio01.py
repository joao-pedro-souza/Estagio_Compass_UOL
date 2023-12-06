with open('number.txt', encoding='utf-8') as arquivo:
    arquivo = arquivo.read().strip().split('\n')
    
    números = [int(número) for número in arquivo]
    
    números_pares = list(map(lambda número: número if número % 2 == 0 else None,números))
    números_pares = list(filter(lambda número: número is not None, números_pares))
    cinco_maiores = sorted(números_pares, reverse=True)[:5]
    soma_números = sum(cinco_maiores)
    
    print(cinco_maiores)
    print(soma_números)
    