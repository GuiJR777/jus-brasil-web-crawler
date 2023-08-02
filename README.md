# Jus Brasil web Crawler

Este é um guia passo a passo para instalar e executar o projeto FastAPI com Redis, que pode ser feito manualmente ou usando o Docker.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

- Python 3.11 ou superior (para execução manual)
- Docker e Docker Compose (para execução com Docker)

## Instalação e Execução Manual

1. Clone o repositório

   ```
   git clone https://github.com/GuiJR777/jus-brasil-web-crawler
   cd jus-brasil-web-crawler
   ```
2. Crie um ambiente virtual (opcional, mas recomendado)

   ```
   python -m venv venv
   source venv/bin/activate (Linux/Mac) ou venv\Scripts\activate (Windows)
   ```
3. Instale as dependências

   ```
   pip install -r requirements.txt
   ```
4. Configurando as variáveis de ambiente

   Crie um arquivo `.env` no diretório raiz do projeto e adicione as seguintes variáveis de ambiente:

   ```
   REDIS_URL=redis
   REDIS_PORT=6379
   REDIS_PASS=sua_senha_do_redis (se aplicável, deixe em branco caso não tenha senha)
   REDIS_TTL=3600
   ```
5. Inicie a API

   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   Agora, a API FastAPI estará em execução em `http://localhost:8000`.

## Instalação e Execução com Docker

1. Clone o repositório

   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie um arquivo `.env` no diretório raiz do projeto e adicione as seguintes variáveis de ambiente:

   ```
   REDIS_URL=redis
   REDIS_PORT=6379
   REDIS_PASS=sua_senha_do_redis (se aplicável, deixe em branco caso não tenha senha)
   REDIS_TTL=3600
   ```
3. Execute o Docker Compose

   ```
   docker-compose up --build
   ```

   Isso criará e executará os contêineres necessários para a API FastAPI e o servidor Redis. A API estará acessível em `http://localhost:8000`.

## Encerrando a Execução

Se você estiver usando o Docker, basta pressionar `Ctrl+C` para parar a execução dos contêineres. Em seguida, você pode executar o seguinte comando para remover os contêineres:

```
docker-compose down
```

Se você estiver executando manualmente, basta pressionar `Ctrl+C` para interromper o servidor Uvicorn.

## Testes Unitários

Para rodar os testes basta instalar as dependencias de desenvolvedor com o comando
 ```
   pip install -r requirements-dev.txt
 ```
e depois o comando
 ```
   pytest
 ```

## Utilização

Para utilizar após executar no docker ou no manual acesse seu localhost na porta 8000:
```
http://0.0.0.0:8000
```
No endpoint `/status` você terá um health check.

No endpoint `/docs` você terá a documentação online da API.

No endpoint `/consult` você deverá fazer uma requisição do tipo POST com o seguinte corpo
```
{
  "numero_processo": "string"
}

# Numero de exemplo:

{"numero_processo": "0710802-55.2018.8.02.0001"}
```

e você obterá um json com a seguinte estrutura com os dados do processo:
```
{
  "status": "ok",
  "message": "string",
  "data": {
    "grau_1_data": {
      "classe": "string",
      "area": "string",
      "assunto": "string",
      "data_de_distribuicao": "string",
      "juiz": "string",
      "valor_da_acao": 0,
      "partes_do_processo": {
        "advogados_apelada": [],
        "advogados_apelado": [],
        "advogados_apelante": [],
        "advogados_autor": [],
        "advogados_reu": [],
        "apelada": "string",
        "apelado": "string",
        "apelante": [],
        "autor": "string",
        "custos_legis": "string",
        "reu": "string",
        "terceiros": [],
        "testemunhas": [],
        "vitima": "string"
      },
      "lista_das_movimentacoes": [
        {
          "data": "string",
          "details": "string"
        }
      ]
    },
    "grau_2_data": {
      "classe": "string",
      "area": "string",
      "assunto": "string",
      "data_de_distribuicao": "string",
      "juiz": "string",
      "valor_da_acao": 0,
      "partes_do_processo": {
        "advogados_apelada": [],
        "advogados_apelado": [],
        "advogados_apelante": [],
        "advogados_autor": [],
        "advogados_reu": [],
        "apelada": "string",
        "apelado": "string",
        "apelante": [],
        "autor": "string",
        "custos_legis": "string",
        "reu": "string",
        "terceiros": [],
        "testemunhas": [],
        "vitima": "string"
      },
      "lista_das_movimentacoes": [
        {
          "data": "string",
          "details": "string"
        }
      ]
    }
  }
}
```
