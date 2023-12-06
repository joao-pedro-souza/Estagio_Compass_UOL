def conta_vogais(texto:str)-> int:
    texto = texto.lower()
    texto = list(filter(lambda letra: letra in 'aeiou', texto))
    
    return len(texto)

