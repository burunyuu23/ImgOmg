FROM python:3.11

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && pip install -r ./requirements.txt

EXPOSE 5001

CMD ["python", "main.py", "5001"]