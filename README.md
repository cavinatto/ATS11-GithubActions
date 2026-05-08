# ATS11 GitHub Actions

Este repositório contém uma API Python com FastAPI e um pipeline de Integração Contínua (CI) configurado com GitHub Actions.

## Estrutura

- `main.py` - API FastAPI com rotas para leitura raiz, soma e multiplicação.
- `test_main.py` - testes automatizados com `pytest` para validar as rotas.
- `.github/workflows/ci.yml` - workflow do GitHub Actions que executa testes e um teste de integração.
- `requirements.txt` - dependências do projeto.

## Como funciona o CI

O workflow `Teste de API` roda em duas situações:

- `push`
- `pull_request`

Ele executa o job `verificar-api` com matrix de Python:

- `3.10`
- `3.11`
- `3.12`

Passos do workflow:

1. Faz checkout do código.
2. Instala a versão de Python do matrix.
3. Instala dependências via `requirements.txt`.
4. Roda `pytest test_main.py`.
5. Inicia a API em background com Uvicorn.
6. Verifica a rota raiz e a rota `/somar/10/20` com `curl`.

## Como testar localmente

1. Crie e ative seu ambiente virtual:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode os testes:

```bash
pytest -q
```

4. Opcional: execute a API localmente:

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

## Rotas disponíveis

- `GET /` - verifica se a API está funcionando.
- `GET /somar/{a}/{b}` - soma dois números.
- `GET /multiplicar/{a}/{b}` - multiplica dois números.

## Observações

O pipeline foi configurado para proteger a branch `main` e garantir que o código só seja mesclado após o sucesso dos testes.
