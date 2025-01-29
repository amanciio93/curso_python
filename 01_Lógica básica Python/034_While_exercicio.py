# Qual letra mais aparece na frase: 
frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guid Van Rossum.'
#count() método stringo para contar o número de ocorrências do parametro passado;
# print(frase.count('Python'))
#Lembrando que STRING é iterável, então vamos usar o WHILE para percorre- la;
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase): 
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f"Letra '{letra_apareceu_mais_vezes}' apareceu mais vezes. Total de {qtd_apareceu_mais_vezes} ocorrências")

""" 
    Vamos passar por cada linha do código para entender detalhadamente o que está acontecendo:
1. Declaração de variáveis iniciais

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

    i = 0: Esta variável i será usada como um índice para percorrer cada caractere da string frase.
    qtd_apareceu_mais_vezes = 0: Esta variável armazenará o número de ocorrências da letra que aparece mais vezes na string.
    letra_apareceu_mais_vezes = '': Esta variável armazenará a letra que mais apareceu na string.

2. Início do laço while

while i < len(frase):

    Este laço while vai iterar sobre a string frase, caractere por caractere, até o índice i alcançar o tamanho da string (len(frase)).

3. Pegando o caractere atual

    letra_atual = frase[i]

    Aqui, a variável letra_atual recebe o caractere na posição i da string frase. Isso permite verificar e comparar a letra em cada iteração.

4. Ignorando espaços em branco

    if letra_atual == ' ':
        i += 1
        continue

    Se o caractere atual for um espaço (' '), o laço simplesmente avança para o próximo caractere, ignorando o espaço.
    i += 1: Incrementa i para mover para o próximo caractere.
    continue: Faz com que a iteração atual do while seja interrompida e a próxima iteração seja iniciada imediatamente, ignorando o código abaixo.

5. Contando as ocorrências da letra atual

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    O método count() é usado para contar quantas vezes a letra_atual aparece em toda a string frase. O valor é armazenado em quantas_vezes_letra_apareceu_atual.

6. Verificando se a letra atual é a mais frequente até agora

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

    Aqui, o código verifica se o número de ocorrências da letra_atual é maior do que o número de ocorrências da letra mais frequente encontrada até o momento (qtd_apareceu_mais_vezes).
        Se for maior, a variável qtd_apareceu_mais_vezes é atualizada para o novo valor (o número de ocorrências da letra_atual), e a variável letra_apareceu_mais_vezes é atualizada para a letra que apareceu mais vezes até aquele momento.

7. Incrementando o índice para a próxima iteração

    i += 1

    Incrementa i para avançar para o próximo caractere da string.

8. Exibindo o resultado

print(f"Letra '{letra_apareceu_mais_vezes}' apareceu mais vezes. Total de {qtd_apareceu_mais_vezes} ocorrências")

    Após o laço while terminar, o código imprime qual letra apareceu mais vezes na frase, junto com o número total de ocorrências dessa letra.

Exemplo de execução passo a passo:

Considere que a string frase seja:

frase = "abacadae"

    Primeira iteração (i = 0): letra_atual = 'a'
        quantas_vezes_letra_apareceu_atual = 4 (porque 'a' aparece 4 vezes)
        qtd_apareceu_mais_vezes é atualizado para 4 e letra_apareceu_mais_vezes para 'a'.

    Segunda iteração (i = 1): letra_atual = 'b'
        quantas_vezes_letra_apareceu_atual = 1 (porque 'b' aparece 1 vez)
        Não atualiza as variáveis, pois 1 é menor do que 4.

    Terceira iteração (i = 2): letra_atual = 'a'
        quantas_vezes_letra_apareceu_atual = 4 (porque 'a' aparece 4 vezes)
        Não atualiza, pois a contagem não mudou.

    Quarta iteração (i = 3): letra_atual = 'c'
        quantas_vezes_letra_apareceu_atual = 1 (porque 'c' aparece 1 vez)
        Não atualiza.

    E assim por diante...

No final da execução, o programa determinará que a letra 'a' foi a mais frequente e imprimirá:

Letra 'a' apareceu mais vezes. Total de 4 ocorrências

Considerações finais:

    Eficiência: O código utiliza o método count() em cada iteração, o que pode ser ineficiente para strings grandes. Cada chamada do count() percorre toda a string para contar as ocorrências da letra, o que resulta em uma complexidade O(n²) no pior caso (onde n é o tamanho da string).
    Solução mais eficiente: Uma alternativa mais eficiente seria usar um dicionário para armazenar as ocorrências de cada caractere enquanto percorre a string uma única vez.

Se precisar de mais detalhes ou otimizações, me avise! 😊
"""