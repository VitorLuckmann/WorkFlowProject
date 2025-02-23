from fastapi import FastAPI

# Criando a instância do aplicativo FastAPI
app = FastAPI()

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Hello, GitHub Actions!"}

# Rota para somar dois números
@app.get("/soma/{a}/{b}")
def sum_numbers(a: int, b: int):
    return {"result": a + b}

# Rota para subtrair dois números
@app.get("/subtrai/{a}/{b}")
def subtract_numbers(a: int, b: int):
    return {"result": a - b}

# Rota para multiplicar dois números
@app.get("/multiplica/{a}/{b}")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}

# Rota para dividir dois números (com verificação para evitar divisão por zero)
@app.get("/divide/{a}/{b}")
def divide_numbers(a: int, b: int):
    if b == 0:
        return {"error": "Divisão por zero não é permitida"}
    return {"result": a / b}
