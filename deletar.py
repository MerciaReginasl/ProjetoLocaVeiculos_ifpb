import sqlite3

conn = sqlite3.connect('LocaVeiculos.db')
cursor = conn.cursor()

cod_cliente = 100

# excluindo um registro da tabela
cursor.execute("""DELETE FROM clientes WHERE cod_cliente = ? """, (cod_cliente,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()
