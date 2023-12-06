from csv import reader

with open('estudantes.csv', encoding='utf-8') as arquivo:
    
    leitor_csv = reader(arquivo)
    alunos = []
    notas = []
    
    for linha in leitor_csv:
        alunos.append(linha[0])
        notas.append([int(linha[1]), int(linha[2]), int(linha[3]), int(linha[4]), int(linha[5])])

    tres_maiores = list(map(lambda lista: sorted(lista, reverse=True)[0:3], notas))
    media = list(map(lambda n: round(sum(n)/3, 2), tres_maiores))
    
    lista = []
    
    for i, aluno in enumerate(alunos):
        lista.append([aluno, tres_maiores[i], media[i]])
        
    for l in sorted(lista):
        print(f'Nome: {l[0]} Notas: {l[1]} Média: {l[2]}')
