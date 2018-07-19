# Importar a biblioteca
from sqlite3 import*

# Estabeleça uma conexão com um banco de dados
# LocaVeiculos = Este arquivo em disco é usado para manter o banco de dados e suas tabelas
# Criamos uma classe "generica" chamada connect() que representa o bd

conn=connect('LocaVeiculos.db')

# cursor: é um interador que permite navegar e manipular os registros do bd.
# Execute: lê e executa comandos SQL puro diretamente no bd.
# Crie um cursor para os dados
c=conn.cursor()

# Declare suas funções
def clientes():

    print('Digite os dados pessoais do cliente: ')

    print()

    cod_cliente = input("Digite a sua identificação: ")
    nome = str(input("Digite seu nome: "))
    e_mail = input("Digite seu e-mail: ")
    #Execute um SQL
    c.execute('INSERT INTO clientes VALUES("'+cod_cliente+'","'+nome+'","'+e_mail+'")')

    print('Dados  do cliente inseridos com sucesso!')

    print()

def carros():

    print()

    print('Digite os dados do veiculo a ser reservado: ')

    print()

    placa = input("Digite as referências da placa: ")
    modelo = input("Digite o modelo do carro: ")
    cor = input("Digite a cor do carro: ")
    #Execute um SQL
    c.execute('INSERT INTO carros VALUES("'+placa+'","'+modelo+'","'+cor+'")')

    print()
    
    print('Dados do veiculo inseridos com sucesso!')

    
clientes()
carros()

# O commit diz para sua conexão aplicar todas as manipulações de sua SQL para seus dados e torná-las permanentes
conn.commit()



