# OPERADOR in = ESTÁ ENTRE
# OPERADOR not in = NÃO ESTÁ ENTRE;
# OBS: Strings em Python são ITERÁVEIS ( Pode- se navegar item por item em uma palavra ou frase.)

# 0 1 2 3 4 5 6 7 
# J O N A T H A N 
#-8-7-6-5-4-3-2-1


nome = "Jonathan"

print(nome[2]) # Acessa a posição 2 e traz a letra N;
print(nome[-6]) # Acessa a posição -6 e raz a letra N;

print("nat" in nome)
print("cio" in nome)

print("nat" not in nome)
print("cio" not in nome)