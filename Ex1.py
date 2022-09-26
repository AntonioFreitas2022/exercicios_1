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
min_vendas = 1000
max_vendas = 0
total_vendas = 0
def min_max_vendas(min_vendas,max_vendas):


    if vendas < min_vendas:
        min_vendas=vendas
    if vendas > max_vendas:
        max_vendas = vendas

    return min_vendas
    return max_vendas






list_vendas =[]
list_ilhas = []
n = int(input('Inserir numero de vendas distintas'))

for x in range(0,n):


    vendas = int(input('Inserir valores'))
    ilhas = str(input('Inserir ilhas'))
    total_vendas = total_vendas + vendas


    list_vendas.append(vendas)
    list_ilhas.append(ilhas)
print(min_max_vendas(min_vendas, max_vendas))
print(list_vendas)
print(list_ilhas)

print(f'O max de vendas foi {max_vendas}')
print(f'O min de vendas foi {min_vendas}')
print(f'A média das vendas é {total_vendas/n}')
print(f'O total das vendas é {total_vendas}')



