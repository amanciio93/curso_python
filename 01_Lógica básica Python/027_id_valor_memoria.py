# O Python é uma linguagem inteligente, então ele não cria dois espaços na memória para armazenar o mesmo valor, ele usa um único espaço e informa esse endereço quando for pedido.

v1 = 'a'
v2 = 'a'

v3 = 'b'

print(id(v1))
print(id(v2))

print(id(v3))