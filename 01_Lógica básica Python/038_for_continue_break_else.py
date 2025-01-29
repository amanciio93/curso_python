for i in range(8): # 8 ou 10
    if i == 2:
        print("i é 2, pulando...")
        continue
    if i == 8:
        print("i é 8, else não funcionará!")
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('FOR completo com sucesso!')