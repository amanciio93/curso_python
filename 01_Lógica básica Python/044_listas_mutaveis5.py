# Cuidados com dados mutáveis

nome = 'Jonathan' # IMUTÁVEL !!!
print(nome)
nome = 'Dionatan'
print(nome)

# AS DUAS VARIAVEIS APONTAM PARA O MESMO ENDEREÇO NA MEMÓRIA, B NÃO COPIA A; SÓ QUANDO FOR TIPO MUTÁVEL;
""" listaA = ['Jonathan', 'Dara']
listaB = listaA

print(listaA, listaB)
listaA.append('Luma')
print(listaA, listaB) """


# CASO EU QUEIRA FAZER UMA CÓPIA E NÃO APONTAR PARA O MESMO ENDEREÇO DE MEMÓRIA;
listaA = ['Jonathan', 'Dara']
listaB = listaA.copy()

print(listaA, listaB)
listaA.append('Luma')
print(listaA, listaB)