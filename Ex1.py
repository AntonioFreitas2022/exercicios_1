"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""
n_min = 0
n_max = 0
total_vendas = 0
contador = 0
#Definir variaveis fora das outras funçoes, declara-as como globais

def min_max_vendas(n_min, n_max):
    for a in range(0, n):
        if a == 0:
            n_max = list_vendas[0]   #Aqui o erro foi o facto de não estares a usar o valor de a, estavas a usar o valor                                 #
            n_min = list_vendas[0]   # x, como este valor é fixo, porque a operaçao 'for' já acabou pela altura que vais
        if list_vendas[a] > n_max:   # usar esta função, logo só estavas a usar um único valor fixo, enquanto o valor de a
            n_max = list_vendas[a]   # passa pela lista completa e faz a comparação devidamente
        if list_vendas[a] < n_min:      #Nota o len de uma lista diz o numero de elementos na lista
            n_min = list_vendas[a]

    return n_max,n_min


list_vendas = []
list_ilhas = []
n = int(input('Inserir numero de vendas distintas'))

for x in range(0, n):
    vendas = int(input('Inserir valores'))
    ilhas = str(input('Inserir ilhas'))
    total_vendas = total_vendas + vendas
    #list_vendas.append(vendas = int(input('Inserir valores')))
    # isto aqui tambem funciona para nao ter que criar multiplas variavveis
    list_vendas.append(vendas)
    list_ilhas.append(ilhas)

n_max,n_min = min_max_vendas(n_min, n_max)
print(f'minimo foi {n_min} maximo foi {n_max}')
print(min_max_vendas(n_min,n_max))
print(list_vendas)
print(list_ilhas)
print(f'A média das vendas é {total_vendas / n}')
print(f'O total das vendas é {total_vendas}')
