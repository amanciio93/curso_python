# Definindo funções
#São trechos de códigos usados para replicar determinadas ações ao longo do seu código. Elas podem receiver valores para parâmetros e retornar valores específicos, porém seu padrão é retornar None;

#    PARAMETRO = VARIAVEL DENTRO DO ()
#    ARGUMENTO = VALOR DA VARIAVEL

nome = 'Jonathan'

# Funcao sem parametros
def saudacao():
    print('Hello world!')
    
saudacao()

# Funcao com passagem de parametro
def ola_usuario(nome):
    print(f'Ola {nome}')
    
ola_usuario(nome)

# Se eu chamo uma funcao sem informar o parametro necessario, eu terei um erro na execuçao do meu codigo. Para resolver issoposso deixar um valor estipulado diretamento no parametro em questao;
def mostra_idade(idade=0):
    print(f'A idade e: {idade}')
    
mostra_idade()
mostra_idade(18)