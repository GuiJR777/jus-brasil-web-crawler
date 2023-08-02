# Definindo a imagem base, você pode usar uma versão específica do Python se preferir
FROM python:3.11

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY requirements.txt /app/
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que a API FastAPI estará escutando
EXPOSE 8000

# Comando para iniciar o servidor Uvicorn
CMD ["uvicorn", "main:api_app", "--host", "0.0.0.0", "--port", "8000"]
