# Argumentos nomeados e nao nomeados em funcoes Python
#    Nomeado = nome  com sinal de igual
#    Nao nomeado = recebe apenas o argumento


def soma(x, y):
    #Definiçao
    print(f'{x=} & {y=}  =>   {x} + {y} = {x + y}' )
    
soma(2, 3)

"""
    Não Nomeados (Posicionais)

Em Python, os argumentos não nomeados, ou argumentos posicionais, são aqueles passados para a função de acordo com a ordem em que os parâmetros foram definidos. Ou seja, a posição de cada argumento importa.

Exemplo:

def soma(a, b):
    return a + b

resultado = soma(3, 5)  # Argumentos não nomeados
print(resultado)  # Saída: 8

Neste caso, a recebe o valor 3 e b recebe o valor 5, porque é assim que os argumentos são passados de acordo com a posição em que são fornecidos. O Python automaticamente associa o primeiro valor ao primeiro parâmetro, o segundo ao segundo, e assim por diante.
Argumentos Nomeados (Keyword Arguments)

Já os argumentos nomeados são passados para a função utilizando o nome do parâmetro ao invés de seguir a ordem. Isso torna o código mais legível e permite que você passe os valores para os parâmetros de forma mais flexível, sem se preocupar com a ordem dos argumentos.

Exemplo:

def soma(a, b):
    return a + b

resultado = soma(b=5, a=3)  # Argumentos nomeados
print(resultado)  # Saída: 8

Aqui, mesmo passando os argumentos na ordem inversa (b=5, a=3), o Python consegue associar corretamente os valores aos parâmetros devido ao uso dos nomes.
Mistura de Argumentos Posicionais e Nomeados

Você pode combinar ambos os tipos de argumentos na mesma função, mas é importante que os argumentos posicionais venham sempre antes dos nomeados. Caso contrário, o Python levantará um erro.

Exemplo:

def soma(a, b, c):
    return a + b + c

resultado = soma(3, b=5, c=2)  # Combinação de argumento posicional e nomeado
print(resultado)  # Saída: 10

Aqui, a=3 é passado como um argumento posicional, enquanto b=5 e c=2 são passados como argumentos nomeados.
Conclusão

    Argumentos não nomeados (posicionais): A ordem dos valores que você passa para a função importa.
    Argumentos nomeados: Você especifica o nome do parâmetro e pode passar os valores fora da ordem, o que torna o código mais legível.
"""