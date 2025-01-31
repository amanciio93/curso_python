# SPLIT - divide uma string e retorna uma lista
# JOIN - une uma string

frase = "   O rato   ,    roeu a roupa   ,  do rei de roma    "

lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas) # Sem strip
# print(lista_frases) # Com strip

frases_unidas = ','.join(lista_frases) # Unindo a frase com ",".
print(frases_unidas)