#mod_armazenamento

dicionario_clientes = {}
dicionario_carros = {}

def cadastrar_cliente(cod_cliente, nome):
 #if not buscar_cliente(cod_cliente):
    dicionario_clientes[cod_cliente] = nome

def processar_cliente(c):
    #c = int(input( "Código do cliente: " ))
    n = input("Nome do cliente: ")
    cadastrar_cliente(n, c)

def imprimir_clientes():
    print(dicionario_clientes)

def buscar_cliente(cod_cliente):
    #print(dicionario_clientes[str(cod_cliente)])
    global dicionario_clientes
#   print(dicionario_clientes)
    return dicionario_clientes[cod_cliente]


def cadastrar_carro(placa, modelo):
    if not buscar_carro(placa):
       dicionario_carros[placa] = modelo

def processar_carro():
    c = input( "placa (ex. PUC2015): " )
    m = input("modelo do carro: ")
    cadastrar_carro(c, m)

def imprimir_carro():
    print(dicionario_carros)

def buscar_carro(placa):
    return placa in dicionario_carros.keys()





