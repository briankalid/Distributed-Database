import mysql.connector

def prueba(cnx):
    cursor=cnx.cursor()
    query=("""describe Clientes""")
    cursor.execute(query)
    return(cursor.fetchall())

