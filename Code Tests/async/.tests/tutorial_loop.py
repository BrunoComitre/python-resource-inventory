import asyncio
import time

################################### EXEMPLO 1 ##################################
'''
# Define a rotina que leva em um future
async def MyCoroutine():
    print ("Minha Corotina")

# Gire um loop de eventos rápido e simples
# e execute até concluir
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(MyCoroutine())
finally:
    loop.close()
'''

# run_forever()que posteriormente executará nosso loop de eventos até que a stop() função seja chamada
# ou podemos chamar run_until_complete(future)e executar apenas nosso loop de eventos até que qualquer futureobjeto que passamos tenha concluído execução.

################################### EXEMPLO 2 ##################################
'''
async def MyWork():
    print("Inicia Trabalho")
    time.sleep(0.5)
    print("Finaliza Trabalho")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(MyWork())
finally:
    loop.close()
'''

################################### EXEMPLO 3 ##################################
'''
async def Work():
    while True:
        await asyncio.sleep(1)
        print("Task Executada")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(Work())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Fechando Loop")
    loop.close()
'''

#################################### EXEMPLO 4 ##################################

async def FirstWorker():
    while True:
        await asyncio.sleep(1)
        print("Primeiro Worker Executado")

async def SecondWorker():
    while True:
        await asyncio.sleep(1)
        print("Segundo Worker Executado")

loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(FirstWorker())
    asyncio.ensure_future(SecondWorker())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Fechando Loop")
    loop.close()
