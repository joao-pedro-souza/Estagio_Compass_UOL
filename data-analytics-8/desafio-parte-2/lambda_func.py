import json
import boto3
import requests
from csv import reader
from datetime import datetime

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    bucket_name = 'data-lake-do-jp'  
    s3_file_name = 'Raw/Local/CSV/Movies/2023/05/25/movies.csv'  
    s3_json_folder_name = 'Raw/Local/TMDB/JSON/2023/05/29/'  
    api_key = ''

    response = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
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

    return {
        'statusCode': 200,
        'body': 'JSON files saved in S3'
    }
