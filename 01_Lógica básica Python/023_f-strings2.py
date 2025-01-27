# FORMATAÇÃO BÁSICA DE STRINGS
#   "s" STRING
#   "d" INT
#   "f" FLOAT
#       ".<Nº DE DIGITOS>f"
#   "X ou x" HEXADECIMAL 
#   ">" ESQUERDA
#   "<" DIREITA
#   "^" CENTRO
#   "+ ou -" SINAL
#   CONVERSION FLAGS "!r !s !a
variavel = "ABCD"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")

print(f"{variavel:*>10}")