import mysql.connector

def prueba(cnx):
    cursor=cnx.cursor()
    query=("""describe Clientes""")
    cursor.execute(query)
    return(cursor.fetchall())

def inDatabase(sucursal,cnxm,cnxp,nombre,ap,am,rfc):
#    existin_morelia=False
 #   existin_patz=False

    cursor=cnxm.cursor()
    query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
    cursor.execute(query,(nombre,ap,am,rfc))

    cursorp=cnxp.cursor()
    query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
    cursorp.execute(query,(nombre,ap,am,rfc))
   
    if len(cursor.fetchall())>0:
        #existin_morelia=True
        print('Ya existe en la base de datos')
        print('Los siguientes datos son correctos?')
        print(cursor.fetchall())
        return True
    
    elif len(cursorp.fetchall())>0:
        print('Ya existe en la base de datos')
        print('Los siguientes datos son correctos?')
        print(cursorp.fetchall())

        
        return True

    
    else:
        cursor.close()
        cursorp.close()
        return False

