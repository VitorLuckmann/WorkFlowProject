from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Testa a rota raiz "/"
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, GitHub Actions!"}

# Testa a soma
def test_sum_numbers():
    response = client.get("/soma/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

# Testa a subtração
def test_subtract_numbers():
    response = client.get("/subtrai/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

# Testa a multiplicação
def test_multiply_numbers():
    response = client.get("/multiplica/10/5")
    assert response.status_code == 200
    assert response.json() == {"result": 50}

# Testa a divisão
def test_divide_numbers():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

# Testa divisão por zero
def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 200
    assert response.json() == {"error": "Divisão por zero não é permitida"}
