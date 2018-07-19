# testar

import mod_interface as gui
import mod_armazenamento as ma0

# Incrementar clientes na opção Buscar cliente
codigo_cliente=0

# início do programa
gui.mensagem_entrada()

while True:
    # exibir menu
    gui.exibir_menu()
    # ler opcao
    opcao = gui.ler_opcao()

    # chamar os serviços dos módulos
    # Neste caso o cod_cliente será incrementado durante o cadastro:

    if opcao == 1:
        codigo_cliente+=1
        ma.processar_cliente(codigo_cliente)

    elif opcao == 2:
        ma.processar_carro()

    elif opcao == 3:
        ma.imprimir_clientes()

    elif opcao == 4:
        ma.imprimir_carro()

    elif opcao == 5:
        #c = int(input("Código do cliente: "))
        n = input('Nome do Cliente: ')
        #print(n)
        print(ma.buscar_cliente(n))

        mensagem = "Cliente(s) foi encontrado(s) com sucesso."
        print(mensagem)


    else:
        if gui.sair(): break


# saída do programa
gui.mensagem_saida()