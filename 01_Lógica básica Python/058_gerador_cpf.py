import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

primeiro_contador_regressivo = 10

#   cpf_informado = '41534845801' # VALIDAR COM 'RE' ou REPLACE...

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
print(f'\t### CPF GERADO: {cpf_gerado} ###')

""" if cpf_informado == cpf_gerado:
    print("\tCPF VÁLIDO!")
else:
    print("\tCPF INVÁLIDO!") """