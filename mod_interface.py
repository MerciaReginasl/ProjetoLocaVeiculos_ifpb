#mod_interface

def ler_opcao():
    opcao = int(input("\nDigite a opção: " ))
    return opcao

def sair():
    entrada = input("Deseja realmente sair (s/n)? ")
    return entrada.lower() == 's'

def exibir_menu():
    print( "+------------------------------+" )
    print( "01 - Cadastrar cliente (cod_cliente, nome)" )
    print( "02 - Cadastrar carro (placa, modelo)")
    print( "03 - Imprimir cliente" )
    print( "04 - Imprimir carro" )
    print( "05 - Buscar cliente" )
    print( "00- Sair..." )
    print( "+------------------------------+" )

def mensagem_saida():
    print( "Sistema encerrado." )

def mensagem_entrada():
    print( "Bem-vindo(a) ao sistema de locadora de Veiculos Regina's." )
    print( "Empresa Regina's Locadora. Ju1ho/2018" )