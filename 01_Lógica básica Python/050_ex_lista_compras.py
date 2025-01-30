""" 
    Faça uma lista de compras com listas, o usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
    Não permita que o programa quebre com erros de indices inexistentes na lista;
"""
lista = []
while True:
    print('## 1 - INSERIR ITEM: ')
    print('## 2 - APAGAR ITEM: ')
    print('## 3 - LISTAR ITENS: ')
    print('## 0 - SAIR DO APP.')
    opcao = int(input('## OPÇÃO: '))
    if opcao == 1:
        item = input("ITEM: ")
        lista.append(item)
    if opcao == 2:
        for i, item in enumerate(lista):
            print(f'\t{i} - {item}')
        item = int(input('APAGAR ITEM: '))
        del lista[item]
    if opcao == 3:
        if lista == []:
            print("Lista vazia - Nada para listar")
        for i, item in enumerate(lista):
            print(f'\t\t{i} - {item}')
    if opcao == 0:
        print("##### FECHANDO A LISTA ! #####")
        break