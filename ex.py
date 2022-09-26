n_invert = ''
n = str(input('Inserir numero inteiro positivo'))
n_char = len(n)
x = len(n)
for x in range(0,n_char):
    n_invert =  n[x] +n_invert #isto inverte porque estamos a meter
                            # os numeros na sequencia contraria atras uns dos outros


print({n_invert})