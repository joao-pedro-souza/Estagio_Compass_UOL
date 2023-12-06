import pandas as pd

atores_pd = pd.read_csv('actors.csv')

# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
print(atores_pd.loc[atores_pd['Number of Movies'] == max(atores_pd['Number of Movies']), ['Actor', 'Number of Movies']])

# Apresente a média da coluna contendo o número de filmes.
print(f'\nAverage Number of Movies\n{atores_pd["Number of Movies"].mean()}')

# Apresente o nome do ator/atriz com a maior média por filme.
print(atores_pd.loc[atores_pd['Average per Movie'] == max(atores_pd['Average per Movie']), ['Actor', 'Average per Movie']])

# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
print(f'\nMost Frequent Movie Frequency\n{atores_pd["#1 Movie"].value_counts().head(1)}')
