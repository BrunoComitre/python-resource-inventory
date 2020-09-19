import time
import multiprocessing

from tasks import get_word_counts

PROCESSES = multiprocessing.cpu_count() -1

def run():
    print(f'RODANDO COM :: {PROCESSES} PROCESSOS!')
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'pride-and-prejudice.txt',
            'heart-of-darkness.txt',
            'frankenstein.txt',
            'dracula.txt'
        ])

        # clean up
        p.close()
        p.join()
    print(f'TEMPO GAST0 :: {time.time() - start:.10f}')

if __name__ == "__main__":
    run()



# Método map_async 
# Existem essencialmente quatro métodos diferentes disponíveis para mapear 
# tarefas para processos. Ao escolher um, você deve levar em conta vários
# argumentos, simultaneidade, bloqueio e ordenação:

# Método	 Multi-args	 Simultaneidade	  Bloqueando	Resultados ordenados
#  map	        Não     	  Sim            Sim              Sim
# map_async	    Não     	  Não            Não              Sim
#  apply	    Sim     	  Não            Sim          	  Não
# apply_async	Sim     	  Sim            Não          	  Não
