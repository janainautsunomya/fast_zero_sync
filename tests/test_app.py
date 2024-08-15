from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapidozero.app import app

# def test_read_root_deve_retornar_ok_e_ola_mundo():
#     client = TestClient(app) #arragen ou organização

#     response = client.get('/') #act ou ação

#     assert response.status_code == HTTPStatus.OK #assert garantir
#     assert response.json() == {'message': 'Olá Mundo!'} #assert


def test_read_root_deve_retornar_ola_mundo():
    client = TestClient(app)  # Arrange -> setar as coisas

    response = client.get('/')  # Act -> replicar a ação que o cliente faria

    # Assert -> assegurar que o comportamento esperado está acontecendo
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! :) </h1>' in response.text
