dicionario = {}
atores_faturamento = []

with open('actors.csv', encoding='utf-8') as arquivo_csv:

    dados = arquivo_csv.read().split('\n')

    with open('etapa-5.txt', 'w', encoding='utf-8') as arquivo_txt:

        for dado in dados[1:]:
            
            if ',' in dado and '"' not in dado:
                dicionario = {'ator': dado.split(',')[0], 'faturamento': dado.split(',')[1]}
                atores_faturamento.append(dicionario)
            
            elif '"' in dado:
                dicionario = {'ator': dado.split('"')[1], 'faturamento': dado.split(',')[2]}
                atores_faturamento.append(dicionario)


        atores_faturamento = sorted(atores_faturamento, key=lambda dicionario: dicionario['faturamento'], reverse=True)

        arquivo_txt.write('Lista de Atores ordenada pelo faturamento bruto total em ordem decrescente:\n')
        arquivo_txt.write('Ator')
        arquivo_txt.write('Faturamento\n'.rjust(30))

        for dicionario in atores_faturamento:
            arquivo_txt.write(f"{dicionario['ator']}".ljust(24))
            arquivo_txt.write(f"{dicionario['faturamento']}\n")
