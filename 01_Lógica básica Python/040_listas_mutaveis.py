# LISTAS EM PYTHON SÃO MUTÁVEIS
# SUPORTA VÁRIOS VALORES DE QUALQUER TIPO
# CONHECIMENTOS REUTILIZÁVEIS - INDÍCES E FATIAMENTO
# MÉTODOS MAIS USADOS: append, insert, pop, del, clear, extend, +

string = 'ABCDE' # CINCO CARACTERES

lista = [32, True, "Jonathan", 1.85]
#ANTES DE INSERIR ELEMENTOS NA LISTA
# print(lista, type(lista))
# print(bool(lista)) # LISTA VAZIA É CONSIDERADA FALSA PARA BOOLEANOS;

# DEPOIS DE INSERIR ELEMENTOS NA LISTA
# print(lista)
# print(bool(lista)) # LISTA COM ITENS É CONSIDERADA TRUE PARA BOOLEANOS;

# LISTAS TEM INDICE
# [0, 1, 2, 3, 3, 4, 6, ...]

#Pegando o valor do indice 2 e usando um método de str nele;
print(lista[2].upper())

# MUDANDO O VALOR NO INDICE
lista [2] = 'Amancio'
print(lista)
print(lista[2].upper())