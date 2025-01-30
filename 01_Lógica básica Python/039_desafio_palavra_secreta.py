""" 
    faça um jogo para o usuário advinhar a palavra secreta. Proponha uma palavra e dê a possibilidade para o usuário digitar apenas uma letra. Ao capturar a letra digitada, confira e a mesma está na palavra secreta.
    Exiba as letras acertadas e exiba *** para as que ainda não foram acertadas.
    Conte o numero de tentativas.
"""

#Importando um módulo
import os
tentativas = 0
palavra_secreta = 'biblia'
letras_acertadas = ''

while True:
    chute = input("Qual letra deseja chutar? ")
    tentativas += 1

    # Validando apenas um caractere por tentativa;
    if len(chute) > 1:
        print("APENAS UMA LETRA POR VEZ !")
        continue # Volta no início do laço;

    # Se o chute for igual a uma letra da palavra secreta, eu armazeno para exibir a cada loop
    if chute in palavra_secreta:
        letras_acertadas += chute

    # Se a letra chutada estiver na palavra, eu exibo essa letra, senão eu exibo * no lugar, Aqui percorremos a string com o operador in;
    palavra_formada = ''
    for chute in palavra_secreta:
        if chute in letras_acertadas:
            palavra_formada += chute
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f"Parabéns, você ganhou após {tentativas} tentativas!.")
        print(f"A palavra secreta era '{palavra_secreta}'")
        break