# Base Image
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências do projeto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o container
COPY . /app/

# Expor a porta 8000
EXPOSE 8000

# Comando de entrada
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
