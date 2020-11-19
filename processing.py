import mysql.connector
import random


def generate_id(UG):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ID = UG
    for x in range(7):
        if (x%2 == 0):
            ID += str(random.randint(0,9))
        else:
            ID += random.choice(letters)

    return(ID)


def prueba(cnx):
    cursor=cnx.cursor()
    query=("""describe Clientes""")
    cursor.execute(query)
    return(cursor.fetchall())

def inDatabase(cnxm,cnxp,nombre,ap,am,rfc):
#    existin_morelia=False
 #   existin_patz=False

    cursor=cnxm.cursor()
    query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
    cursor.execute(query,(nombre,ap,am,rfc))
    resm=cursor.fetchall()

    cursorp=cnxp.cursor()
    query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
    cursorp.execute(query,(nombre,ap,am,rfc))
    resp=cursorp.fetchall()

    if len(resm)>0:
        #existin_morelia=True
        print('Ya existe en la base de datos')
        print('Los siguientes datos son correctos?')
        print(resm)
        return True
    
    elif len(resp)>0:
        print('Ya existe en la base de datos')
        print('Los siguientes datos son correctos?')
        print(resp)

        
        return True

    
    else:
        #cursor.close()
        #cursorp.close()
        return False


def registrar_cliente(cnx,nombre,ap,am,rfc):
    cursor = cnx.cursor()
    id = generate_id("U")
    query = """INSERT INTO Clientes(Id,Nombre,Apellido_Paterno,Apellido_Materno,RFC) VALUES (%s,%s,%s,%s,%s)"""
    data_query = (id,nombre,ap,am,rfc)
    cursor.execute(query,data_query)
    cnx.commit()
    print("Query efectuadas correctamente...")

