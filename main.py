from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API funcionando!"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    # Retorna a soma dos dois números
    return {"resultado": a + b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    # Retorna a multiplicação dos dois números
    return {"resultado": a * b}
