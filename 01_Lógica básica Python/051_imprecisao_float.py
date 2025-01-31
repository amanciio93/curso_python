# Imprecisão de ponto flutuante;
#   Double-precision floating-point format IEEE 754;

import decimal

numero1 = 0.1
numero2 = 0.7

numero3 = numero1 + numero2

print(numero3) # IMPRECISO

print(round(numero3, 1)) # Resolvendo a imprecisão com round.

#Resolvendo com módulo decimal
num1 = decimal.Decimal('0.1')
num2 = decimal.Decimal('0.7')
num3 = num1 + num2

print(num3)