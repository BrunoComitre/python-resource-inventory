# NOTE-APP

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
[5:06 PM] Thiago Brito dos Anjos
    o model é uma representação do tabela
​[5:06 PM] Thiago Brito dos Anjos
    já o db é o objeto q manipula a base


Futuro: Questão de histórico de nota

os dados nao salvam no banco
ao criar a nota preciso passar [ ]
remover id repetido


http://containertutorials.com/docker-compose/flask-mongo-compose.html

https://medium.com/@riken.mehta/full-stack-tutorial-flask-react-docker-ee316a46e876

O __repr__método informa ao Python como imprimir objetos dessa classe, o que será útil para depuração. Você pode ver o __repr__()método em ação na sessão do interpretador Python abaixo:
>>> from app.models import User
>>> u = User(username='susan', email='susan@example.com')
>>> u
<User susan>


</br>

[In Development]

</br>

## TO-DO

- [ ] flask usa blueprint para registrar endpoint
- [ ] manipulação na model
- [ ] no flask blueprint é onde fica a rota e onde chama a model
- [ ] ver como fazer autenticação (bonus)
- [ ] depois subir docker e depois mandar para o deploy
- [ ] export FLASK_APP='main.py' (NAO ESQUECER DE USAR)
- [ ] FLASK RUN EXECUTA A APLICAÇÃO
- [ ] SUBIR NO HEROKU A APLICAÇAO (atraves do arquivo procfile)
- [ ] Fazer [Application Factories](https://www.google.com/search?q=factory+application+-+flask&oq=factory+application+-+flask&aqs=chrome..69i57j0l7.7907j0j7&sourceid=chrome&ie=UTF-8)

<br />

## IMPORTS

 - [flask](https://palletsprojects.com/p/flask/)
 - [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
 - [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
 - [psycopg2-binary](https://www.psycopg.org/docs/install.html)
 - [python-dotenv](https://github.com/theskumar/python-dotenv)

<br />

## HEROKU

ARQUIVO: procfile
COLOCAR: web: gunicorn main:app

ARQUIVO: runtime.txt
COLOCAR: python-3.8.1

<br />

## Notes

### CMD
Run at run time only (Runtime)flask

- Run command on containers during startup
- Equivalent to:
  - <arguments> <command>
  - docker run <arguments> / bin / bash
- One CMD by Dockerfile

**Shell Form**
- Commands are expressed in the same way as shell commands

**Exec Form**

<br />

### EXAMPLE LEVELS
- debug: Logs messages from debug, info, warn, error and fatal.
- info: Logs messages from info, warn, error and fatal.
- warn: Logs messages from warn, error and fatal.
- error: Logs messages from error and fatal.
- fatal: Error messages only fatal.

</br>

***  

</br>
 
## References

- [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas/tree/master/Projects/1-Beginner)
- [Notes App](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Notes-App.md)
- [cookiecutter flask](https://www.google.com/search?q=cookiecutter+flask&oq=cookiecutter+flask&aqs=chrome..69i57j0l7.6670j0j7&sourceid=chrome&ie=UTF-8)
- [Real Python](https://realpython.com/tutorials/flask/)

- [cookiecutter-flask/cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask/tree/master/%7B%7Bcookiecutter.app_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D)
- []()
- []()

***
