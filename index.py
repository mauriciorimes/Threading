import random

random.seed(1)
lista = []
for i in range(10000):
  lista.append(random.randint(0, 1000))
print([lista[i] for i in range(10)])

from threading import Thread 

class Th(Thread):
  lista = []
  total = 0
  def __init__(self, tid, lista):
    Thread.__init__(self)
    self.pid = tid
    self.lista = lista

  def run(self):
    self.total = sum(self.lista)

  def get_total(self):
    return (self.pid, self.total)
  
th = Th(0, lista)
th.start()
total = th.get_total()
print(total)

lista0 = []
lista1 = []

for i in range(len(lista) // 2):
  lista0.append(lista[i]) 
  lista1.append(lista[len(lista) - 1 - i]) 

th0 = Th(0, lista0)
th1 = Th(1, lista1)

th0.start()
th1.start()

print(f'A Thread {th0.get_total()[0]} totalizou {th0.get_total()[1]}')
print(f'A Thread {th1.get_total()[0]} totalizou {th0.get_total()[1]}')

total = th0.get_total()[1] + th1.get_total()[1]
print(f'O resultado final foi: {total}')

