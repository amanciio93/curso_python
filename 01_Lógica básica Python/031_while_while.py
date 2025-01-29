qtde_linhas = 3
qtde_colunas = 3

linha = 1
while linha <= qtde_linhas:
    coluna = 1
    while coluna <= qtde_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1