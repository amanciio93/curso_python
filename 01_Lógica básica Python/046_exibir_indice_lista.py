# EXIBA OS INDICES DA LISTA

listaA = ['Jonathan', 'Dara', 'Videl', 'Gohan', 31, 28, 4, 1] 

""" 
# minha solução
indice = 0
for i in listaA:
    print(f"INDICE: {indice}, VALOR: {i}")
    indice += 1 """

indices = range(len(listaA))

for indice in indices:
    print(indice, listaA[indice])