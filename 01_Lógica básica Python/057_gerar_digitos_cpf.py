"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_informado = '41534845801' # VALIDAR COM 'RE' ou REPLACE...
nove_digitos = cpf_informado[0:9:1]
primeiro_contador_regressivo = 10

soma_primeiros_digitos = 0
for digito in nove_digitos:
    soma_primeiros_digitos += int(digito) * primeiro_contador_regressivo
    primeiro_contador_regressivo -= 1
primeiro_digito = (soma_primeiros_digitos * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)
segundo_contador_regressivo = 11

soma_dez_digitos = 0
for digito in dez_digitos:
    soma_dez_digitos += int(digito) * segundo_contador_regressivo
    segundo_contador_regressivo -= 1
segundo_digito = (soma_dez_digitos * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(f'PRIMEIRO DIGITO: {primeiro_digito} \nSEGUNDO DIGITO: {segundo_digito}')

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_informado == cpf_gerado:
    print("\tCPF VÁLIDO!")
else:
    print("\tCPF INVÁLIDO!")