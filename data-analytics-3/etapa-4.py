filmes = []
aparicoes_filmes = []
filme_mais_aparicoes = ''
c = 0

with open('actors.csv', encoding='utf-8') as arquivo_csv:
    
    dados = arquivo_csv.read().split('\n')

    with open('etapa-4.txt', 'w', encoding='utf-8') as arquivo_txt:

        for dado in dados[1:]:
            
            if ',' in dado and '"' not in dado:
                filmes.append(dado.split(',')[4])
            
            elif '"' in dado:
                filmes.append(dado.split(',')[5])

        arquivo_txt.write('Filme(s) mais frequente(s):\n')
        arquivo_txt.write('Filme') 
        arquivo_txt.write('Frequência (aparições)\n'.rjust(35)) 

        for filme in filmes:
            aparicoes_filmes.append(filmes.count(filme))


        for aparicoes in aparicoes_filmes:
            
            if aparicoes == max(aparicoes_filmes) and filme_mais_aparicoes != filmes[c]:
                arquivo_txt.write(f'{filmes[c]}'.ljust(27))
                filme_mais_aparicoes = filmes[c]
                arquivo_txt.write(f'{aparicoes}\n')
            
            c += 1
