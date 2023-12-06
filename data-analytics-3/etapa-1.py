lista_atores = []
numero_filmes = []

with open('actors.csv', encoding='utf-8') as arquivo_csv:

    dados = arquivo_csv.read().split('\n')
    
    for dado in dados[1:]:
        
        if ',' in dado and '"' not in dado:
            lista_atores.append(dado.split(',')[0])
            numero_filmes.append(dado.split(',')[2])
        
        elif '"' in dado:
            lista_atores.append(dado.split('"')[1])
            numero_filmes.append(dado.split(',')[3])


with open('etapa-1.txt', 'w', encoding='utf-8') as arquivo_txt:
    
    c = 0
    
    arquivo_txt.write('Ator com maior número de filmes:\n')
    arquivo_txt.write('Ator')
    arquivo_txt.write('Número de Filmes\n'.rjust(30))

    for n in numero_filmes:
        
        if n == max(numero_filmes):
            arquivo_txt.write(f'{lista_atores[c]}'.ljust(24))
            arquivo_txt.write(f'{n}')
        
        c += 1
