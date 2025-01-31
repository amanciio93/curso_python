salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Jonathan', 'Dara', 'Gohan', ' Videl']
]

print(salas)

#Percorrendo a primeira lista e depois cada item das sublistas;
for lista in salas:
    print(f"SALA: {lista}")
    for nome in lista:
        print(f"ALUNO: {nome}")