import sqlite3 

connection = sqlite3.connect('LocaVeiculos.db')
c = connection.cursor()

#SQL

sql = 'SELECT *FROM clientes WHERE cod_cliente = ?'

def read_data(wordUsed):
    for row in c.execute(sql, (wordUsed,)):
        print (row)

read_data(500)

#Valores vem em tuplas
