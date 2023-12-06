atores = []
faturamento_medio = []
c = 0

with open('actors.csv', encoding='utf-8') as arquivo_csv:
    
    dados = arquivo_csv.read().split('\n')
    
    with open('etapa-3.txt', 'w', encoding='utf-8') as arquivo_txt:
        
        for dado in dados[1:]:
            
            if ',' in dado and '"' not in dado:
                faturamento_medio.append(float(dado.split(',')[3]))
                atores.append(dado.split(',')[0])
            
            elif '"' in dado:
                faturamento_medio.append(float(dado.split(',')[4]))
                atores.append(dado.split('"')[1])
        

        arquivo_txt.write('Ator com maior faturamento por filme:\n')
        arquivo_txt.write('Ator')
        arquivo_txt.write('Média de Faturamento\n'.rjust(35))


        for faturamento in faturamento_medio:
            
            if faturamento == max(faturamento_medio):
                arquivo_txt.write(f'{atores[c]}'.ljust(25))
                arquivo_txt.write(f'{faturamento}\n')
                break
            
            c += 1
