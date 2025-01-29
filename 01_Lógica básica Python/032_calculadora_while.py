# Calculado com WHILE;

continuar = 's'

while continuar == 's':
        
    numero1 = int(input("Primeiro número: "))
    numero2 = int(input("Segundo número: "))
    operador = input("Operador [ +, -, *, / ]: ")

    if operador == '+':
        print(f"{numero1} + {numero2} = {numero1 + numero2}")
    elif operador == '-':
        print(f"{numero1} - {numero2} = {numero1 - numero2}")
    elif operador == '*':
        print(f"{numero1} * {numero2} = {numero1 * numero2}")
    elif operador == '/':
        print(f"{numero1} / {numero2} = {numero1 / numero2}")
    else:
        print("Operador ou números inválidos.")

    continuar = input("Deseja continuar? S ou N: ")
    if continuar.lower() == 's':
        continue
    elif continuar.lower() == 'n':
        break
    else:
        continuar = 's'
        print("Responde direito babaca!")
        continue