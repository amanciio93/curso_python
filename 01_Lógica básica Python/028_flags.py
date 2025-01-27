# NONE = Não valor / Sem valor
# IS ou IS NONE = É ou NÃO É;

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Fazendo algo...")
else:
    print("Não está fazendo nada...")

if passou_no_if is None:
    print("Não passou no IF")

if passou_no_if is not None:
    print("Passou no IF")

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
