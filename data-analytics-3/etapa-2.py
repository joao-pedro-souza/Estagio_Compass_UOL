with open('actors.csv', encoding='utf-8') as arquivo:
    
    dados = arquivo.read().split('\n')[1:]
    
    with open('etapa-2.txt', 'w', encoding='utf-8') as arquivo_txt:
        
        arquivo_txt.write('Média de faturamento bruto por ator:\n')
        arquivo_txt.write('Ator '.ljust(25))
        arquivo_txt.write('Média de faturamento\n\n')
        
        for dado in dados:
            
            if ',' in dado and '"' not in dado:
                arquivo_txt.write(f"{dado.split(',')[0]}".ljust(25))
                arquivo_txt.write(f" {dado.split(',')[3]}")
                arquivo_txt.write(' \n')
            
            elif '"' in dado:
                arquivo_txt.write(dado.split('"')[1])
                arquivo_txt.write(f" {dado.split(',')[4]}".rjust(14))
                arquivo_txt.write('\n')
