# +=
# -=
# *=
# /=
# //=
# **=
# %=
contador = 0

while contador < 10:
    contador += 1 # contador = contador + 1

    if contador % 2 != 0:
        continue

    print(f"{contador}ª repetição")