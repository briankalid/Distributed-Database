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



def update_cliente(cnx,id):
    still=True
    clt=['Nombre','Apellido_Paterno','Apellido_Materno','RFC']
    while still:
        print('Que desea modificar?')
        print('1. Datos del cliente')
        print('2. Direccion')
        print('3. Dejar de modificar')
        op=int(input())
        if op == 1:
            print('Que datos desea modificar?')
            for i,e in enumerate(clt):
                print(str(i)+'.',e)

            print('Hint: Puedes escoger varias opciones a la vez, ejemplo: 1,2,4')
            lista=[int(i)for i in input().split(',')]
            print(lista)
        






def inDatabase(sucursales,cnxs,nombre,ap,am,rfc):
    for i,cnx in enumerate(cnxs):
        cursor=cnx.cursor()
        query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
        cursor.execute(query,(nombre,ap,am,rfc))
        resp=cursor.fetchall()
        
        if(len(resp))>0:
            print('Ya existe en la base de datos de',sucursales[i])
            print('Los siguientes datos son correctos?')
            print(resp)
            query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""

           

            cursor.execute(query,(resp[0][0],))
            print(cursor.fetchall())
            mod=input('si/no: ')
            
            if mod=='si':
                return True

            else:
                mod=input('Quieres modificarlos? si/no: ')
                if mod == 'si':
                    update_cliente(cnx,resp[0][0])
                else:
                    return True
            #return True
    return False

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

