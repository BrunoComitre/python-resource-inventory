##################### Códigos de status das respostas HTTP #####################
# As respostas são agrupadas em cinco classes:
## - (100-199) : Respostas de informação
## - (200-299) : Respostas de sucesso
## - (300-399) : Redirecionamentos
## - (400-499) : Erros do cliente
## - (500-599) : Erros do servidor
################################################################################

##################### Códigos de status das respostas HTTP #####################

# 200 OK = Requisição bem sucedida. O significado do sucesso varia de acordo com
# o método HTTP

# 201 Created = Requisição foi bem sucedida e um novo recurso foi criado como 
# resultado. Esta é uma tipica resposta enviada após uma requisição POST

# 404 Not Found = O servidor não pode encontrar o recurso solicitado

# 422 Unprocessable Entity (WebDAV) = A requisição está bem formada mas
# inabilitada para ser seguida devido a erros semânticos
################################################################################


import json
import pytest
from app.api.api_v1.endpoints import notes # from app.api import crud


##################################### POST #####################################

def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "something", "description": "something else", "status": "A Fazer"}
    test_response_payload = {"id": 1, "title": "something", "description": "something else", "status": "A Fazer"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(notes, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", data=json.dumps({"title": "something"}))
    assert response.status_code == 422

    response = test_app.post("/notes/", data=json.dumps({"tilte": "1", "description": "2", "status": "A Fazer"}))
    assert response.status_code == 422

##################################### GET ######################################

def test_read_note(test_app, monkeypatch):
    test_data = {"id": 1, "title": "something", "description": "something else", "status": "A Fazer"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(notes, "get", mock_get)

    response = test_app.get("/notes/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(notes, "get", mock_get)

    response = test_app.get("/notes/68")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

    response = test_app.get("/notes/0")
    assert response.status_code == 422

################################### GET ALL ####################################

def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "something", "description": "something else", "id": 1, "status": "A Fazer"},
        {"title": "someone", "description": "someone else", "id": 2, "status": "A Fazer"},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(notes, "get_all", mock_get_all)

    response = test_app.get("/notes/")
    assert response.status_code == 200
    assert response.json() == test_data

##################################### PUT ######################################

def test_update_note(test_app, monkeypatch):
    test_update_data = {"title": "someone", "description": "someone else", "id": 1, "status": "A Fazer"}

    async def mock_get(id):
        return True

    monkeypatch.setattr(notes, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(notes, "put", mock_put)

    response = test_app.put("/notes/1/", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1, {"description": "bar"}, 422],
        [999, {"title": "foo", "description": "bar"}, 404],
        [1, {"title": "1","description": "bar", "status": "A Fazer"}, 422],
        [1, {"title": "foo","description": "1"}, 422],
        [0, {"title": "foo","description": "bar", "status": "A Fazer"}, 422],
    ],
)
def test_update_note_invalid(test_app, monkeypatch, id, payload, status_code):
    async def mock_get(id):
        return None

    monkeypatch.setattr(notes, "get", mock_get)

    response = test_app.put(f"/notes/{id}/", data=json.dumps(payload),)
    assert response.status_code == status_code

#################################### DELETE ####################################

def test_remove_note(test_app, monkeypatch):
    test_data = {"title": "something", "description": "something else", "id": 1, "status": "A Fazer"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(notes, "get", mock_get)

    async def mock_delete(id):
        return id

    monkeypatch.setattr(notes, "delete", mock_delete)

    response = test_app.delete("/notes/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_note_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(notes, "get", mock_get)

    response = test_app.delete("/notes/68/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"
    
    response = test_app.delete("/notes/0/")
    assert response.status_code == 422
