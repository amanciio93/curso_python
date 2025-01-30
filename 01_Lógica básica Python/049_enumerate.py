# ENUMERAT() - Enumera iteráveis (Indices)

listaA = ['Jonathan', 'Dara', 'Videl', 'Gohan']

lista_enumerada = enumerate(listaA)

# ITERADOR
""" print(lista_enumerada)
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))
 """

""" for item in lista_enumerada:
    print(item) """

for item in enumerate(listaA):
    print(item)