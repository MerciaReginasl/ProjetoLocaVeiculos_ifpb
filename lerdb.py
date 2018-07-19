import pymysql


def main(arg):

    # Abrindo uma conexão com o banco de dados

    bd = pymysql.connect(host='localhost',
                             user='root',
                             password='Regina78',
                             db='LocaVeiculos',
                             charset='utf8mb4',
                             unix_socket='/opt/lampp/var/mysql/mysql.sock',
                             cursorclass=pymysql.cursors.DictCursor)

    # Instancia um objeto cursor utilizando o método cursor

    cursor = bd.cursor()

    # Esta senteça SQL seleciona toda a tabela clientes:
    sql = "SELECT * FROM clientes"

    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # Ler todas as linhas da tabela.
        linhas = cursor.fetchall()

        print(linhas)

        for linha in linhas:
            cod_cliente = linha['cod_cliente']
            nome = linha['nome']
            e_mail = linha['e_mail']

        # Imprima, no terminal, os valores lidos de interesse
            print('O codigo do cliente: ', cod_cliente)
            print('O nome do cliente: ', nome)
            print('O e- mail do cliente: ', e_mail)


    except:
        print('Erro: Impossível obter dados.')

    # fecha a conexão
    bd.close()

