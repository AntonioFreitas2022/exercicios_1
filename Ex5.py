"""
Peça ao utilizador para inserir uma frase
Após o utilizador ter inderido a frase apresente:
 - Imprima a frase, mas com cada palavra invertida.
 Por exemplo a frase é 'Bom dia!' deve dar 'moB !aid'
  Imprime a frase mas com as maisculas em minisculo e vice versa
 - Quantas palavras tem a frase
 - Quantas vogais tem a frase
 - Quantas letras maiusculas tem a frase
 - Quantas letras minusculas tem a frase
 - Quantos numeros tem a frase
 - Apresente a frase invertida. Exemplo: A frase é 'Bom dia!' deve dar '!aid moB'
"""

vogal_counter = 0
vogal_checker = 0
num_checker = 0
num_counter = 0
lowercase_counter = 0
uppercase_counter = 0

sentence = input('Inserir frase')
comprimento_frase = len(sentence)
palavras_frase = len(sentence.split(' '))
palavras_separadas = sentence.split(' ')
sentence_min = sentence.lower()
sentence_mais = sentence.upper()
list_palavras_invert = []
list_palavras = []

list_frase = []
list_frase_maisculaminuscula = []
list_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sentence_invert = ''
palavra_invert = ''

# inverter cada uma das palavras na frase
for y in range(0, palavras_frase):
    list_palavras.append(palavras_separadas[y])

    for a in range(0, len(list_palavras[y])):
        palavra_actual = list_palavras[y]
        palavra_invert = palavra_actual[a] + palavra_invert  # Aqui eu quero inverter o cada uma das palavras mas em ordem. COnsigo trocar a ordem das palavras, mas não estou a conseguir inverter a palavra em si
    str(list_palavras_invert.append(' ' + palavra_invert))
    palavra_invert = ''
# inverter as maisculas por minusculas na frase, e minusculas por maisculas na frase

for b in range(0, comprimento_frase):
    if str.isupper(sentence[b]) == True:
        list_frase_maisculaminuscula.append(sentence_min[b])
    if str.isupper(sentence[b]) == False:
        list_frase_maisculaminuscula.append(sentence_mais[b])

print(*list_frase_maisculaminuscula)



for x in range(0, comprimento_frase):
    sentence_invert = sentence[x] + sentence_invert
    # n_invert = str(n_invert + n[x])

for n in range(0, len(sentence)):
    list_frase.append(sentence[n])

    vogal_checker = list_frase[n]

    for num_checker in list_num:
        num_checker = list_frase[n]
        if any(elem in num_checker for elem in list_num):
            num_counter += 1
            break

    if vogal_checker == 'a' or vogal_checker == 'e' or vogal_checker == 'i' or vogal_checker == 'o' or vogal_checker == 'u' or vogal_checker == 'U' or vogal_checker == 'O' or vogal_checker == 'I' or vogal_checker == 'E' or vogal_checker == 'A':
        vogal_counter += 1  # Existe alguma forma de fazer com que seja igual a todas estas condições?
    if str.isupper(list_frase[n]):
        uppercase_counter += 1
    if not str.isupper(list_frase[n]) and list_frase[n] != ' ' and list_frase[n] != list_num:
        lowercase_counter += 1

print(f'characteres frase= {comprimento_frase} palavras na frase= {palavras_frase} '
      f'vogais na frase= {vogal_counter} numeros na frase= {num_counter} frase invertida= {sentence_invert} '
      f'maisculas na palavras = {uppercase_counter} minusculas na palavras = {lowercase_counter - num_counter}')
print('Caracteres invertidos, mas nao a posicao das palavras')
print(*list_palavras_invert)
