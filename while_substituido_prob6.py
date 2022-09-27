# MAIOR OU IGUAL AO PRIMEIRO
# MOSTRA TODOS OS NUMEROS PRIMOS QUE HÁ ENTRE O PRIMEIRO E O SEGUNDO
# DEPOIS DE MOSTRAR OS NUMEROS DIZ QUANTOS NUMEROS PRIMOS HAVIA

# criar uma versao deste programa que não usa o ''for''. ambos na funçao
# e na parte do if __name__. Nem um unico for.
# ALterar o for para while


if __name__ == '__main__':
    ini = int(input('Inserir numero inicial'))
    fim = int(input('Inserir numero final'))
    primos = 0
    contador = ini
    contador2 = 1
    zeros = 0

while contador < fim:
    while contador2 < contador+1:
        if contador % contador2 == 0:
            zeros += 1  # Isto incrementa zeros por um | zeros + 1
        contador2 += 1

    if zeros == 2:

            primos += 1
            print(contador)


    contador2 = 1
    contador += 1
    zeros = 0

print(f'Entre {ini} e {fim} há {primos} primos')