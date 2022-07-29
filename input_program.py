#Programma per la gestione molteplice di Thread in modo che uno produca un risultato usato dall'altro,
#Utilizzo di due array input e output (riconducibile al problema del produttore - consumatore ).
from threading import Thread
from queue import Queue

in_q = Queue()
out_q = Queue()

numbersOfCycles = 10

def squarer():
    while True:
        x = in_q.get()
        if x is None: # signal to terminate
            return
        out_q.put(x**2) # put answer

def bar():
    for x in (range(numbersOfCycles)):
        in_q.put(x)
        result = out_q.get()
        print(f'{x}**2 = {result}')

t1 = Thread(target=squarer)
t1.start()
t2 = Thread(target=bar)
t2.start()
t2.join()
in_q.put(None) # signal thread to terminate
t1.join()
