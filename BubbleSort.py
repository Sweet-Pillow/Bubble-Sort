from random import randint, seed
import matplotlib.pyplot as plt

lista = []
seed()


def exibir(lt, tempo):
    plt.cla()
    plt.clf()
    plt.title('Bubble Sort')
    plt.ylim(0, 100)
    plt.xlim(0, len(lt))
    plt.bar(range(0, len(lt)), lt)
    plt.pause(tempo)


for n in range(0, 10):
    lista.append(randint(0, 100))
    print(f'{lista[n]} ', end='')
else:
    print('')

plt.ion()
exibir(lista, 1)

check = True

while check:
    check = False
    for n in range(0, len(lista) - 1):
        if lista[n] > lista[n + 1]:
            a = lista[n + 1]
            lista[n + 1] = lista[n]
            lista[n] = a
            check = True
        exibir(lista, 0.01)

plt.ioff()

for n in lista:
    print(f'{n} ', end='')
