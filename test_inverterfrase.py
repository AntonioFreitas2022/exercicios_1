sentence = input('Inserir frase')
comprimento_frase = len(sentence)

palavras_frase = len(sentence.split(' '))
palavras_separadas = sentence.split(' ')

list_palavras_invert =[]
list_palavras = []
list_frase = []
palavra_invert = ''

# inverter cada uma das palavras na frase
for y in range(0 ,palavras_frase):
    list_palavras.append(palavras_separadas[y])

    for a in range(0, len(list_palavras[y])):
        palavra_actual = list_palavras[y]
        palavra_invert = palavra_actual[a] + palavra_invert    # Aqui eu quero inverter o cada uma das palavras mas em ordem. COnsigo trocar a ordem das palavras, mas não estou a conseguir inverter a palavra em si
    str(list_palavras_invert.append(' ' + palavra_invert))
    palavra_invert = ''

print(f'Lista palavras inver {list_palavras_invert}')
print(*list_palavras_invert)