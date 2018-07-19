import sqlite3

conn = sqlite3.connect('LocaVeiculos.db')
cursor = conn.cursor()

placa = 'BRA2018'

# excluindo um registro da tabela
cursor.execute("""DELETE FROM carros WHERE placa = ? """, (placa,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()
