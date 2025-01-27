# Introdução ao try/except
#   TRY -> Tenta executar um trecho de código;
#   EXCEPT -> Ocorreu algum erro ao tentar executar;5


numero_str = input("Informe o número à dobrar: ")


try:
    print("STR Inserida: ", numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f"O dobro de {numero_float} é: {numero_float * 2}")
except:
    print("Isso não é um número!")