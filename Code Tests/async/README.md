# Learning Async

</br>

## TO-D0

- [ ] Criar Dockerfile e docker-compose
- [ ] Definir ambientes de teste, produção e desenvolvimento
- [ ] Documentar chamadas das rotas

</br>

## Começando

Caso precise achar o PATH do Pipenv: $ pipenv --venv

</br>

### Notas

```
Future sempre são chamadas de baixo nível aguardando chamada de alto nível.
​Um Future representa um resultado final de uma operação assíncrona.
O Future é um objeto de mais baixo nível

A Task é de alto nível
A Task é um objeto que é agendado para ser executado no event loop

O Event Loop, essencialmente, tem a finalidade de aguardar a ocorrência de 
eventos antes de corresponder cada evento a uma função que correspondemos 
explicitamente ao tipo de evento.
O Event Loop registrar, executar e cancelar chamadas
O Event Loop Iniciar subprocessos e transportes associados para comunicação com um programa externo
O Event Loop Delegar chamadas de função dispendiosas a um conjunto de threads

Tanto o Future quanto a Task, são uma Task

O Event Loop é o gerenciador de Tasks
```

</br>

## Referências

- [Tutorial de loops de eventos assíncronos](https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/)
- [asyncio — Asynchronous I/O](https://docs.python.org/pt-br/3/library/asyncio.html)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [Event Loop](https://docs.python.org/pt-br/3/library/asyncio-eventloop.html)
- [Futures](https://docs.python.org/pt-br/3/library/asyncio-future.html)
- [heapq — Heap queue algorithm](https://docs.python.org/pt-br/3/library/heapq.html)
- []()
- []()
- []()
- []()
  
***
