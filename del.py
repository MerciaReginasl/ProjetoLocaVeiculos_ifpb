# Deletando uma linha

import pymysql

def main(args):

     # Abrindo uma conexão com banco de dados

    bd = pymysql.connect(host='localhost',
                         user='root',
                         password='Regina78',
                         db='LocaVeiculos',
                         charset='utf8',
                         unix_socket='/opt/lampp/var/mysql/mysql.sock',
                         cursorclass=pymysql.cursors.DictCursor)

# Instancia um objeto cursor utilizando o metodo cursor

    cursor = bd.cursor()

# Esta sentença SQL atualiza todas as linhas do banco de dados.
# No caso so temos uma linha:

    sql = "DELETE FROM clientes WHERE nome= 'Mércia Regina da Silva'"

    try:
         # Execute o comando SQL
        cursor.execute(sql)
         # Confirme:
        bd.commit()

    except:
        print('Erro: Impossível atualizar dado(s).')
        # Cancela operações
        bd.rollback()

        # Fecha a conexão
        bd.close()

        return 0





if _name_ == "_main_":
    import sys
    sys.exit(main(name))




