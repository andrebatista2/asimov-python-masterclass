FROM python:3.12.1-slim
WORKDIR /app

COPY . .
RUN apt update && apt install curl -y && rm -Rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt

EXPOSE 8001
HEALTHCHECK CMD curl --fail http://localhost:8001/_stcore/health  #Comando enviado ao Docker para verificar a condição do container, em caso de parada
ENTRYPOINT ["python3", "main.py"]