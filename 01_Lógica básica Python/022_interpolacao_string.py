# Interpolação básica de strings

#   "s" para strings
#   "d" e "i" para int
#   "f" para float
#   "x" e "X" para hexadecimal

nome = "Jonathan"
salario = 3.100
frase = "%s ganha R$%.3f por mês" % (nome, salario)
print(frase)

# HEXADECIMAL = ABCDEF0123456789

frase2 = "O hexadecimal de %d é %08x" % (1500, 1500)
print(frase2)