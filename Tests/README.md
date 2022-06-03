# Testing in Python

- [Live de Python #75 - Testes de unidade](https://www.youtube.com/watch?v=Sr9lUR1COpU&list=PLOQgLBuj2-3K1hb7XgkGPb4S9YNIeHsPk&index=87)
- [Live de Python #76 - Testes de unidade p.II - Dublês de teste](https://www.youtube.com/watch?v=mOrsJwY2038&list=PLOQgLBuj2-3K1hb7XgkGPb4S9YNIeHsPk&index=83)
- [Live de Python #80 - Melhorando testes de unidade](https://www.youtube.com/watch?v=HuZ2Keoc9Hs)

contunuar através da documentação: test_fixtures.py

**[start commands]**

- create poetry: `$ poetry init`
- install: `$ poetry add pytest`
- run: `$ poetry shell`
- test: `$ pytest`

**[used links]**

- [Pytest: Uma introdução - Live de Python #167](https://www.youtube.com/watch?v=MjQCvJmc31A)
- [Pytest Fixtures - Live de Python #168](https://www.youtube.com/watch?v=sidi9Z_IkLU)

**[study links]**

- [How to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html)
- [Working with custom markers](https://docs.pytest.org/en/latest/example/markers.html)
- [How to use skip and xfail to deal with tests that cannot succeed](https://docs.pytest.org/en/7.1.x/how-to/skipping.html)
- [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/6.2.x/fixture.html)
- [Parametrizing fixtures and test functions](https://docs.pytest.org/en/6.2.x/parametrize.html)

**[livros recomendados]**

- Test-Driven Development - Kent Beck
- Growing Objected-Oriented Software, Guided by Tests - Steve Freeman and Nat Pryce
- xUnit Tets Patterns - Gerard Meszaros
- Unit Testing - Vladmir Khorikov
- Python Testing with Pytest - Brian Okken
- pytest Quick Start Guide - Bruno Oliveira

**[comandos pytest]**

- pytest -v : (verbose) mostra o nome dos testes executados
- pytest -s : Mostra as saídas no console
- pytest -k "guava" : (keyword) roda apenas os testes que tem a keyword no nome
- pytest -m tag : (mark) roda apenas os testes que tem a tag mark específica
- pytest -m "not tag" : (mark) roda apenas os testes que não tem a tag mark específica
- pytest -x : Para no teste que falhou
- pytest --pdb enter depois 'atributo ou algo a se ver no debug' enter : Para no teste que falhou em modo debbuger
- pytest --junitxml report.xml : Armazenar op histórico (Gera Report)
- pytest -rs : Mostra o motivo de ter skipado
- pytest --fixtures : Exibe todas as fixtures dispopníveis e as criadas pelo desenvolvedor

**[resumo de erros]**

- . : Passou
- F : Falhou
- x : Falha Esperada
- X :Falha Esperada, mas não Passou
- s : Pulou (Skiped)

**[tags embutidas]**

- @mark.skip : Para pular um teste
- @mark.skipif : Para pular um teste em determinado contexto
- @mark.xfail : É esperado que este teste falhe em algum contexto
- @mark.usefixture : Resoluções e fixação de falhas recorrentes
- @mark.parametrize : Para parametrizar testes com argumentos

**[fixtures disponíveis]**

- capsys e variações : "Espiona" o stdout
- tempdir : Cria um diretório temporário
- caplog : "Espiona" logs
- monKeypatch : Adiciona atributos e métodos a objetos em runtime

**[escopo]**

- function : Antes e depois de cada função
  - não é compartilhada
  - default
- class
- module
- package
- session

---
