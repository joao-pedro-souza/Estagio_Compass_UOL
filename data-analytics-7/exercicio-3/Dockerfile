FROM python:3

RUN pip install boto3

WORKDIR /app

COPY . .

CMD ["python", "upload.py"]