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

def inDatabase(sucursales,cnxs,nombre,ap,am,rfc):
    for i,cnx in enumerate(cnxs):
        cursor=cnx.cursor()
        query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
        cursor.execute(query,(nombre,ap,am,rfc))
        resp=cursor.fetchall()
        
        if(len(resp))>0:
            print('Ya existe en la base de datos de',sucursales[i])
            print('Los siguientes datos son correctos?')
            
            query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""
            cursor.execute(query,(resp[0][0],))
            print(cursor.fetchall())
 
            return True



#    existin_morelia=False
 #   existin_patz=False

# cursor=cnxm.cursor()
# query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
# cursor.execute(query,(nombre,ap,am,rfc))
# resm=cursor.fetchall()

# cursorp=cnxp.cursor()
# query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
# cursorp.execute(query,(nombre,ap,am,rfc))
# resp=cursorp.fetchall()
# print(resp)
# if len(resm)>0:
#     #existin_morelia=True
#     print('Ya existe en la base de datos')
#     print('Los siguientes datos son correctos?')
#     query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""
#     cursor.execute(query,(resm[0][0],))
#     print(cursor.fetchall())

#     return True
# 
# elif len(resp)>0:
#     print('Ya existe en la base de datos')
#     print('Los siguientes datos son correctos?')
#     query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""
#     cursorp.execute(query,(resp[0][0],))
#     print(cursorp.fetchall())

#     
#     return True

# 
# else:
#     #cursor.close()
#     #cursorp.close()
#     return False


def registrar_cliente(cnx,nombre,ap,am,rfc,calle,col,est,cp):
    cursor = cnx.cursor()
    id = generate_id("U")
    query = """INSERT INTO Clientes(Id,Nombre,Apellido_Paterno,Apellido_Materno,RFC) VALUES (%s,%s,%s,%s,%s)"""
    data_query = (id,nombre,ap,am,rfc)
    cursor.execute(query,data_query)
    cnx.commit()
    query = """INSERT INTO Direcciones(Calle,Colonia,Estado,CP,Id_Cliente) VALUES(%s,%s,%s,%s,%s)"""
    data_query=(calle,col,est,cp,id)
    cursor.execute(query,data_query)
    cnx.commit()
    print('Cliente registrado con exito')

