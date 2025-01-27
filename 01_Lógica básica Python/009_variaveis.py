# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: Inicie as variáveis sempre com letras minúsculas, pode usar números e underline.
# PEP8 (Gui de estilos do código Python)
# O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a uma variável.
# EX:
#   nome = "Jonathan"

nome = "Jonathan"
nome_completo = "Jonathan Amancio Vieira Coelho da Silva"

ano_atual = 2025

dia_nasc = 11
mes_nasc = 3
ano_nasc = 1993
data_nasc = "11/03/1993"

idade = ano_atual - ano_nasc

peso = 93.00
altura = 1.85

imc = peso / (altura ** 2)

print("Nome completo: ", nome_completo)
print("Idade: ", idade)
print("Peso: ", peso, "Kg")
print("Altura: ", altura, "cm")
print("IMC: ", float(imc))