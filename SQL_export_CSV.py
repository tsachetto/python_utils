import psycopg2
import sys

#Autoral by --tsachetto--

# Definição da conexão com a DB onde informo o nome, o usuário, a senha e o IP.
conn = psycopg2.connect("dbname=? user=? password=? host=?")

# Abertura de conexão para execução de queryes.
cur = conn.cursor()

# Query de consulta da tabela empresa. columns=None
#DEFINA O DIRETORIO E O ARQUIVO DE LOG
f = open("diretorio", "w")
cur.copy_to(f, 'schema.tabela', sep=';', null='')
f.close()

# Fechar conexão com a DB.
cur.close()
conn.close()
