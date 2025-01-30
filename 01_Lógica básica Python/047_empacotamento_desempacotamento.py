# Introdução ao desempacotamento + tuples ( TUPLAS );

listaA = ['Jonathan', 'Dara', 'Videl', 'Gohan']

#Desempacotamento
nome1, nome2, nome3, nome4 = listaA
print(nome1)
print(nome2)
print(nome3)
print(nome4)

idade1, idade2, idade3, idade4 = [31, 28, 4, 1]
print(idade1) 
print(idade2) 
print(idade3) 
print(idade4) 

# Empacotamento
profissao1, *_resto = ['enfermeiro', 'vendedora', 'cão de guarda', 'cão de guarda']
print(profissao1) # enfermeiro

_, profissao2, *_resto = ['enfermeiro', 'vendedora', 'cão de guarda', 'cão de guarda']
print(profissao2) # vendedora