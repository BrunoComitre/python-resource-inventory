# LINKS PARA ABRIR

- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [Projeto de APIs RESTful com NodeJS e Restify](https://code.tutsplus.com/pt/tutorials/restful-api-design-with-nodejs-restify--cms-22637)

- [Desenvolvendo e testando uma API assíncrona com FastAPI e Pytest](https://testdriven.io/blog/fastapi-crud/#routes)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [HTTPie](https://httpie.org/)
- [Introduction to ASGI: Emergence of an Async Python Web Ecosystem](https://florimond.dev/blog/articles/2019/08/introduction-to-asgi-async-python-web/)
- [Docker for Python Developers](https://mherman.org/presentations/dockercon-2018/#1)
- [Find, install and publish Python packages with the Python Package Index](https://pypi.org/)
- [Tutorial básico de SQLAlchemy](https://leportella.com/tutorial-basico-sqlalchemy.html)
- [Tipos de coluna e dados](https://docs.sqlalchemy.org/en/13/core/type_basics.html)
- [Pytest - Monkeypatching/mocking modules and environments](https://docs.pytest.org/en/latest/monkeypatch.html)
- [Pypi - Find, install and publish Python packages with the Python Package Index](https://pypi.org/)

- [Documentation](http://localhost:8002/docs)
- [Documentation](http://localhost:8002/redoc)
- [pgAdmin](http://localhost:16543/)

docker-compose exec web pytest .

***



usar tortoise orm que tem pydantic



# Learning FastAPI

![version](https://img.shields.io/badge/version-0.0.1-blue.svg?maxAge=2592000)

Elaboração de um escopo de projeto para teste

IMPLEMENTAR : [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/)

ESTUDAR : [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)

ESTUDAR : [Sibling package imports](https://stackoverflow.com/questions/6323860/sibling-package-imports/50193944#50193944)

DEIXAR SEMPRE ABERTO : [Python 3 - 6. Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)

IMPLEMENTAR NOTAS : [Funções em Python: entendendo parâmetros, argumentos, *args e **kwargs](https://medium.com/luizalabs/fun%C3%A7%C3%B5es-em-python-entendendo-par%C3%A2metros-argumentos-args-e-kwargs-4291b1f817f6)

ESTUDAR : 
- [Usando anotações de tipo do Python](https://dev.to/dstarner/using-pythons-type-annotations-4cfe#:~:text=Type%20Annotations%20are%20a%20new,to%20the%20dynamically%20typed%20Python.)
- [Dicas para digitar dicas (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Verificação de tipo Python (Guia)](https://realpython.com/python-type-checking/)
- [typing — Support for type hints](https://docs.python.org/3/library/typing.html)

LER SOBRE : [mypy](http://mypy-lang.org/)


</br>

## TO-D0

- [ ] Criar Dockerfile e docker-compose
- [ ] Definir ambientes de teste, produção e desenvolvimento
- [ ] Documentar chamadas das rotas

</br>

## Começando

Caso precise achar o PATH do Pipenv: $ pipenv --venv

Rodar o servidor uvicorn: $ uvicorn main:app --reload

Rodar o Vue:
- $ cd number-client
- $ npm run serve

### Documentar chamadas HTTP

- [Swagger](https://swagger.io/) - O Swagger é uma estrutura de software de código aberto apoiada por um grande ecossistema de ferramentas que ajuda os desenvolvedores a projetar, criar, documentar e consumir serviços da Web RESTful.

</br>

### Visão Geral da Arquitetura

```
exemplo/
├── api = API e documentação
├── cmd = utilitários e acessórios
├── infra = arquivos de configuração usados ​​pelos servidores de temporariedade e produção
├── lambda = lambda functions
├── scripts = scripts de shell usados ​​pelo CI / CD e outras tarefas administrativas
├── workers = trabalhadores que consomem filas SQS
│
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── routes.py
│   └── models.py
```

</br>

## Referências

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Pypi FastAPI](https://pypi.org/project/fastapi/)
- [Github FastAPI](https://github.com/tiangolo/fastapi)
- [FastAPI + Vue.JS — Integração Python/JavaScript](https://medium.com/@marciobbarbosa/fastapi-vue-js-integra%C3%A7%C3%A3o-python-javascript-ddab7e6905a4)
- [Pydantic Field Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [Python Shallow Copy and Deep Copy](https://www.programiz.com/python-programming/shallow-deep-copy)
- [HTTPX Requests Compatibility Guide](https://www.python-httpx.org/compatibility/)
- [Códigos de status de respostas HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status)
- [Sphinx Python Documentation Generation](https://www.sphinx-doc.org/en/master/index.html)

***
