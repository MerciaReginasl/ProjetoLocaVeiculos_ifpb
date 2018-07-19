import pymysql

def main():

    #Abrindo uma conexão com o banco de dados.

    bd = pymysql.connect(host='localhost',
                             user='root',
                             password='Regina78',
                             db='LocaVeiculos',
                             charset='utf8mb4',
                             unix_socket='/opt/lampp/var/mysql/mysql.sock',
                             cursorclass=pymysql.cursors.DictCursor)

    # Instancia um objeto cursor utilizando o método cursor:
    cursor = bd.cursor()

    # Gere uma consulta SQL solicitando a versão do banco de dados:
    cursor.execute("SELECT VERSION()")

    # Capture o resultado em uma única linha:
    versao = cursor.fetchone()
    print("Versão do gerenciador Maria DB : " '%s', versao)

    # Fecha a conexão:
    bd.close()

    return 0

if __name__ == ' __main__':
    import sys
    sys.exit(main())
