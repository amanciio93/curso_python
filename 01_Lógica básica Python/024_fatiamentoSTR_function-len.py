# Fatiamento de strings

# 0 1 2 3 4 5 6 7 8 
# O l á m u n d o !
#-9-8-7-6-5-4-3-2-1

# Fatiamento [INICIO:FINAL:PASSO] [::]
# OBS: A função len() retorna a quantidade de caracteres da string

variavel = 'Olá mundo!'
print(variavel[4:8:1]) # mund

#Omitindo o final, ele corta até o final
print(variavel[4:]) # mundo!

#Omitindo o iniicio, ele inicia o corte do 0.
print(variavel[:4:1]) #Olá 

print(len(variavel)) #10
print(len(variavel[4:8:1])) #4 
print(len(variavel[4:])) #6
print(len(variavel[:4:1])) #4