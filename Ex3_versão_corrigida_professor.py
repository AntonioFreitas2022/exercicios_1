"""
Complete o programa

Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios

Nota: Parece que afinal o numero de numeros aleatorios não era o intervalo e simplesmente e não estava definido
O professor indicou que seria geralmente impossivel sem definir este problema.
Tambem indicou que existe situaçoes qu não temos toda a informaçao, e que e importante identificar

Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""



#ver github prof

import random


# def divisores(numero):
#    zeros = 0
#
#    for n in range(1, numero + 1):
#        if numero % n == 0:
#            zeros += 1  # Isto incrementa zeros por um | zeros + 1
#    return zeros


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    ini = int(input('n1'))
    fim = int(input('n2'))
    print(ini, fim)
    pares = 0
    impares = 0
    primos = 0
    tipo = str(input('pares impares ou primos'))
    if tipo == 'pares':
        pares = 1
    elif tipo == 'impares':
        impares = 1

    else:
        primos = 1

    for x in (ini, fim + 1):
        n_aleatorio = random.randrange(ini, fim + 1)
        print(n_aleatorio)
        print(x)

        if pares == 1:
            if n_aleatorio % 2 == 0:
                print(n_aleatorio)




        # elif impares == 1:
        #    if n_aleatorio % 2 != 0:
        #        print('n_aleatorio')
        #    else:
        #        for n in range(ini, fim + 1):
        #            if divisores(n) == 2:
        #                print(n)
