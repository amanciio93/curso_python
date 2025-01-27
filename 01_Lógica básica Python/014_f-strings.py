# Utilizando f-strings

nome = "Jonathan"
idade = 31
sexo = "M"
peso = 93.00
altura = 1.85
imc = peso / (altura ** 2)

# print("IMC = ", imc)

print(f"O usuário {nome} tem {idade} anos e é do sexo {sexo}.")
print(f"Seu peso é de {peso} Kg e sua altura é de {altura}, logo seu IMC é de {imc:.2f}")