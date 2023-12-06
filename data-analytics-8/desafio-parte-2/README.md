# Desafio - Parte II

Neste desafio meu objetivo foi extrair e guardar informações da API do TMDB em arquivos JSON, 
para que futuramente possa usar essas informações para completar as informações já existentes no arquivo movies.csv, que foi enviado para um bucket S3 na sprint 7.

O primeiro passo para concluir o desafio foi criar uma conta no [The Movie Database](https://www.themoviedb.org/?language=pt-BR) e uma chave de acesso para sua *API*. 
Com a chave da API eu consegui fazer requisições para o site do TMDB e receber dados dos filmes e pude proseguir no desafio.

Comecei então a desenvolver o código para concluir o desafio, importando as bibliotecas necessárias.

```
import boto3
import requests
from csv import reader
from datetime import datetime
```

Comecei a desenvolver meu código utilizando a bilioteca boto3, para acessar o arquivo movies.csv dentro do S3.

```
s3_client = boto3.client('s3')
bucket_name = 'data-lake-do-jp'  
s3_file_name = 'Raw/Local/CSV/Movies/2023/05/25/movies.csv'  

response = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
```

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/3e22a3fd-6fe8-4008-80d7-2994ca4f7e02)

Para que o boto3 acesse o arquivo dentro do bucket, precisei criar uma função no IAM para que o Lambda tenha acesso ao S3:

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/445ce3bf-89a5-4915-9faf-a4bf206fec14)

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/1639d016-5dff-4416-87d4-026b97f5ca9a)


Também defini a pasta onde eu queria que meus arquivos JSON fossem salvos

`s3_json_folder_name = 'Raw/Local/TMDB/JSON/2023/05/29/'`

Abri o arquivo movies.csv para ler o id do filme, que eu usei para substituir na url e assim conseguir fazer requisições para conseguir suas informações,
fiz um if para que o programa só busque os ids dos filmes de Ação e Aventura, que é o tema do desafio da minha squad. A requisição só será feita se o ID do filme no 
arquivo csv seja diferente da que está armazenada na variável, para evitar a repetição de requisições. Então, após a requisição, se ela tiver sucesso, ou seja, 
ter o response.status_code == 200, o conteúdo dessa requisição seria armazenado para ser gravado no arquivo JSON.

```
csv_filmes = response['Body'].read().decode('utf-8').splitlines()

total_linhas = len(csv_filmes)
contador = 0
id = ''
json_buffer = []

for indice, linha in enumerate(reader(csv_filmes, delimiter='|')):
    if 'Action,Adventure' in linha[5]:
        if id != linha[0]:
            id = linha[0]
            url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=pt-BR"
            response = requests.get(url)
            if response.status_code == 200:
                movie_data = json.loads(response.text)
                json_buffer.append(movie_data)
                contador += 1
```

Criei uma variável contador que aumenta a cada requisição bem sucedida, isso por que cada arquivo JSON deveria conter somente 100 requisições.
Após 100 requisições, o programa usa o with open para salvar as informações em um arquivo JSON. Criei uma lógica para que no começo do arquivo sejam abertos colchetes **( [ )** 
e ao final fossem fechados colchetes **( ] )**, além de por uma vírgula ao final de cada registro, isso para respeitar as regras dos arquivos JSON para evitar erros.
Ao final de tudo o arquivo era gravado com o nome json_data + o horário em que o arquivo foi escrito, isso para evitar conflitos e que os arquivos fossem sobreescritos na execução do programa.
Ao final de tudo, o programa limpa a variável json_buffer, que estava guardando as informações dos filmes até elas serem escritas no arquivo JSON, além de limpar a variável contador, para que o programa voltasse a ser executado até 100 requisições terem sucesso novamente.

```
if contador == 100 or indice == total_linhas - 1:
      timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
      json_file_name = f'movies_data_{timestamp}.json'
      json_file_path = f'/tmp/{json_file_name}'

      with open(json_file_path, 'w', encoding='utf-8') as json_file:
          json_file.write('[')
          json_file.write('\n')
          for i, item in enumerate(json_buffer):
              if i > 0:
                  json_file.write(',')
                  json_file.write('\n')
              json.dump(item, json_file, ensure_ascii=False)

          json_file.write('\n')
          json_file.write(']')

      s3_json_file_name = s3_json_folder_name + json_file_name
      s3_client.upload_file(json_file_path, bucket_name, s3_json_file_name)

      json_buffer = []
      contador = 0
```

Após verificar tudo e confirmar que o programa estava funcionando localmente, foi a vez de executar o código no Lambda. Criei uma nova função Lambda, utilizando Python.
Tive que fazer algumas alterações para o código funcionar no Lambda, como colocar todo a lógica dentro da função **lambda_handler**.

`def lambda_handler(event, context):`

Além de definir uma mensagem caso o programa fosse executado corretamente:

```
return {
        'statusCode': 200,
        'body': 'JSON files saved in S3'
    }
```

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/c99ea20e-018b-4d83-a2b2-31470b99b0c0)

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/d5abd49e-00f7-4557-8c6c-aa9bb67f68aa)

Após executar a função Lambda com sucesso, os arquivos JSON foram enviados para o bucket no S3.

![image](https://github.com/joaopedrocompass/Compass/assets/126081326/f0511854-082d-473c-9932-ecde13648e69)
