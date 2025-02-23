from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, GitHub Actions!"}

def test_sum_numbers():
    response = client.get("/soma/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}
