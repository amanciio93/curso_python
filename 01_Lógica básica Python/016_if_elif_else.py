# IF = SE
# ELIF = SENÃO SE
# ELSE = SENÃO

# Usamos if, elif e else para criar uma estrutura condicional, dependando da condição tomamos caminhos diferentes.

numero = int(input("Informe um número inteiro qualquer: "))

if numero > 5:
    print("Maior que 5")
elif numero < 5:
    print("Menor que 5")
else:
    print("O número é 5")