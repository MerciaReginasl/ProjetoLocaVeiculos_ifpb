# Abrindo uma conexão com o banco de dados
# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  locaveiculoscg_1.py
#

import pymysql


def main(args):
    # Abrindo uma conexão com o banco de dados

    bd = pymysql.connect(host='localhost',
                         user='root',
                         password='Regina78',
                         db='locaveiculoscg',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    # instancia um objeto cursor utilizando o método cursor
    cursor = bd.cursor()

    # gere uma consulta SQL solicitando a versão do banco de dados.
    cursor.execute("SELECT VERSION()")

    # Capture o resultado em uma única linha.
    versao = cursor.fetchone()
    print("Versão do gerenciador Maria DB : %s " % versao)

    # fecha a conexão
    bd.close()

    if __name__ == "__main__":
        import sys
        sys.exit(main(args))
