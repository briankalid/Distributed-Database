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



def update_cliente(cnx,datos,datos_dom):
    still=True
    datos=list(datos)
    datos.append(datos[0])
    datos_dom=list(datos_dom)
    clt=['Nombre','Apellido_Paterno','Apellido_Materno','RFC']
    dr=['Calle','Colonia','Estado','CP']

    while still:
        print('Que desea modificar?')
        print('1. Datos del cliente')
        print('2. Direccion')
        print('3. Dejar de modificar')
        op=int(input())
        if op == 1:
            print('Que datos desea modificar?')
            for i,e in enumerate(clt):
                print(str(i+1)+'.',e)
            
            print(str(len(clt)+1)+'. Regresar')
            print('Hint: Puedes escoger varias opciones a la vez, ejemplo: 1,2,4\n')
            lista=[int(i)for i in input().split(',')]
            
            aux=[]
            dataux=[]
            for elemento in lista:
                if elemento ==len(clt)+1:
                    break
                else:
                    aux.append(clt[elemento-1])
            for i,e in enumerate(aux):
                dataux.append(input('Nuevo '+e+': '))

            query="""UPDATE Clientes SET Id = %s, Nombre = %s, Apellido_Paterno = %s, Apellido_Materno = %s, RFC = %s WHERE id=%s"""
            for i,elemento in enumerate(lista):
                datos[elemento]=dataux[i]
            data_query=tuple(datos)
            cursor=cnx.cursor()
            cursor.execute(query,data_query)
            cnx.commit()
            print('Actualizacion exitosa')

        elif op == 2:
            print('Que datos desea modificar?')
            for i,e in enumerate(dr):
                print(str(i+1)+'.',e)
            print(str(len(dr)+1)+'.Regresar')
            print('Hint: Puedes escoger varias opciones a la vez, ejemplo: 1,2,4\n')
            lista=[int(i) for i in input().split(',')]
            
            aux=[]
            dataux=[]
            for elemento in lista:
                if elemento ==len(dr)+1:
                    break
                else:
                    aux.append(dr[elemento-1])
            for i,e in enumerate(aux):
                dataux.append(input('Nuevo '+e+': '))

            query="""UPDATE Direcciones SET Calle = %s, Colonia = %s, Estado = %s, CP = %s WHERE Id_Cliente=%s"""
            for i,elemento in enumerate(lista):
                datos_dom[elemento-1]=dataux[i]
            data_query=tuple(datos_dom)
            cursor=cnx.cursor()
            cursor.execute(query,data_query)
            cnx.commit()
            print('Actualizacion exitosa')

        else:
            still=False
            





def inDatabase(sucursales,cnxs,nombre,ap,am,rfc):
    for i,cnx in enumerate(cnxs):
        cursor=cnx.cursor()
        query="""SELECT * FROM Clientes Where Nombre=%s and Apellido_Paterno=%s and Apellido_Materno=%s and RFC=%s"""
        cursor.execute(query,(nombre,ap,am,rfc))
        resp=cursor.fetchall()
        
        if(len(resp))>0:
            print('Ya existe en la base de datos de',sucursales[i],'\n')
            print('Los siguientes datos son correctos?\n')
            print(resp)
            query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""

           

            cursor.execute(query,(resp[0][0],))
            datos=cursor.fetchall()
            print(datos)
            mod=input('\nsi/no: ')
            
            if mod=='si':
                return True

            else:
                mod=input('\nQuieres modificarlos? si/no: ')
                if mod == 'si':
                    update_cliente(cnx,resp[0],datos)
                    return True
                else:
                    return True
            return True
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



def all_client(sucursales,cnxs):
    for i,cnx in enumerate(cnxs):
        cursor = cnx.cursor()
        query="""SELECT * FROM Clientes"""
        cursor.execute(query)
        for elemento in cursor.fetchall():
            print(sucursales[i],elemento)





def buscar_cliente(cnxs,nombre=None,ap=None,am=None,rfc=None,calle=None,colonia=None,estado=None,cp=None):
    for i,cnx in enumerate(cnxs):
        cursor=cnx.cursor()
        if nombre:
            query="SELECT * FROM Clientes WHERE Nombre = '%s' and Apellido_Paterno ='%s' and Apellido_Materno='%s'" %(nombre,ap,am)
            cursor.execute(query)
            clientes=cursor.fetchall()
            if len(clientes)>0:    
                print('Cual es?\n')

                for j,cliente in enumerate(clientes):
                    print(str(i+1)+'.',cliente)

                res=int(input())
                query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""

               

                cursor.execute(query,(clientes[res-1][0],))
                datos=cursor.fetchall()
                
                print('\n',datos,'\n')
                mod=input('\nQuieres modificarlos? si/no: ')
                if mod == 'si':
                    update_cliente(cnx,clientes[res-1],datos)
                else:
                    break

            else:
                print('No se encontro')
            break

        elif rfc:
            query="SELECT * FROM Clientes WHERE RFC = '%s'" %rfc
            cursor.execute(query)
            clientes=cursor.fetchall()
            print('es este show',list(clientes[0]))
            if len(clientes)>0:    
                print('Cual es?')

                for j,cliente in enumerate(clientes):
                    print(str(i+1)+'.',cliente)

                res=int(input())
                query="""SELECT * FROM Direcciones Where Id_Cliente=%s"""

               

                cursor.execute(query,(clientes[res-1][0],))
                datos=cursor.fetchall()
                
                print('\n',datos,'\n')
                mod=input('Quieres modificarlos? si/no: ')
                if mod == 'si':
                    update_cliente(cnx,clientes[res-1],datos)
                else:
                    break
            else:
                print('No se encontro')
 
            break

            



        elif calle:


            
            query="SELECT * FROM Direcciones WHERE Calle = '%s' and Colonia = '%s' and Estado = '%s' and CP = %s" %(calle,colonia,estado,cp)
            cursor.execute(query)
            clientes=cursor.fetchall()
            if len(clientes)>0:    
                print('Cual es?\n')

                for j,cliente in enumerate(clientes):
                    print(str(i+1)+'.',cliente,'\n')

                res=int(input())
                query="""SELECT * FROM Clientes Where Id=%s"""

               

                cursor.execute(query,(clientes[res-1][-1],))
                datos=cursor.fetchall()
                
                print(datos,'\n')
                mod=input('\nQuieres modificarlos? si/no: ')
                if mod == 'si':
                    update_cliente(cnx,datos[res-1],clientes)
                else:
                    break
            else:
                print('No se encontro')
 
            break

            
