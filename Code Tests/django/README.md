# Tutorial Django

[Escrevendo seu primeiro app Django, parte 1](https://docs.djangoproject.com/pt-br/3.0/intro/tutorial01/)

[django-tutorial](https://github.com/jruizvar/django-tutorial)

Lembre-se deste guia de três passos para fazer mudanças nos seus modelos:
- Mude seus modelos (em models.py).
- Rode python manage.py makemigrations para criar migrações para suas modificações
- Rode python manage.py migrate para aplicar suas modificações no banco de dados.

***

## Projeto

Nesse projeto meu projeto em si, aonde tenho minha aplicação é chamada de mysite (PROJETO), ou seja este é o nome do meu projeto

Nesse projeto meu projeto em si, aonde tenho minha aplicação é chamada de products (APLICAÇÃO), ou seja este é o nome onde rodo a minha aplicação

Para criar o projeto: django-admin startproject 'nome do projeto'
Para criar a aplicação: django-admin startapp 'noma da aplicação'

Primeiro passo é registrar a aplicação dentro do projeto:
 - mysite/settings.py em INSTALED_APPS.

Segundo passo é criar as urls
 - mysite/urls.py em definir a rota da sua aplicação.

Terceiro passo, com a url definida, vai em:
- products/urls.py
E defina toda as urls e rotas do seu projeto

Quarto passo, criar as views:
- products/views.py
As views são o que respondem as requests

Quinto passo, criar as models:
Dentro do projeto existem as models, e é aqui onde é definido os objetos do banco de dados.

Sexto passo, os templates:
É aqui onde o render devolve o templete web

Para rodar o projeto: python manage.py makemigrations, e depois
Para rodar o projeto: python manage.py migrate



***

## Links de ajuda

- (Models)[https://docs.djangoproject.com/pt-br/3.0/topics/db/models/#module-django.db.models]
- (django-admin and manage.py)[https://docs.djangoproject.com/pt-br/3.0/ref/django-admin/]
- (Configurações do Django)[https://docs.djangoproject.com/pt-br/3.0/topics/settings/#django-settings]
- (Despachante de URL)[https://docs.djangoproject.com/pt-br/3.0/topics/http/urls/]
- (How to deploy with ASGI)[https://docs.djangoproject.com/pt-br/3.0/howto/deployment/asgi/]
- (Como implementar com WSGI)[https://docs.djangoproject.com/pt-br/3.0/howto/deployment/wsgi/]
- (django2-CRUD-30min)[https://github.com/Gpzim98/django2-CRUD-30min/blob/master/products/templates/prod-delete-confirm.html]
- (Django 2 - CRUD completo em 30 minutos ( 2018 ))[https://www.youtube.com/watch?v=mbQVVIqSxoI]
- ()[]
- ()[]
- ()[]
- ()[]
- ()[]

***


## TO-DO

- [] Aplicar Template Method
- [] Aplicar os padrões nas funções

***
