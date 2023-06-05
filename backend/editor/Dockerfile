FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt \
    && apt-get update \
    && apt-get install -y libgl1-mesa-glx

EXPOSE 5001

CMD ["python", "main.py", "5001"]