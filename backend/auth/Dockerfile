FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 5002
CMD ["python", "main.py", "danilkk", "123", "danilkk_db", "5002"]