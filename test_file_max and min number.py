n = int(input('inserir n '))

lista_1 =[]
lista_2 = []
contador = 0
n_max = 0
n_min = 0
for x in range(0,n):

    contador = input('inserir numero')
    lista_1.append(contador)
    if x == 0:
        n_max = lista_1[0]
        n_min = lista_1[0]

    if lista_1[x] > n_max:
        n_max = lista_1[x]
    if lista_1[x] < n_min:
        n_min = lista_1[x]

print(lista_1)
print(n_max)
print(n_min)