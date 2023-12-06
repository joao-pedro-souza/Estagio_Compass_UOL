def funcao(*args, parametro_nomeado=None, x=None):
    for item in args:
        print(item)
    if parametro_nomeado is not None:
        print(parametro_nomeado)
    if x is not None:
        print(x)
    
    
funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
