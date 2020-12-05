import mysql.connector
import random
import database

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




def buscar_clientes(sucursales,cnxs):
    clt=['Nombre','Apellido_Paterno','Apellido_Materno']
    dr=['Calle','Colonia','Estado','CP']
    datos=[]

    print ("\n\t Buscar cliente por: \n 1.- Nombre \n 2.- RFC \n 3.- Domicilio \n 4.- Listado Completo")
    try: 
        opcion_busqueda = int(input())

        if opcion_busqueda==1:

            print('Elige tus criterios de busqueda')
            for i,e in enumerate(clt):
                print(str(i+1)+'.',e)
            
            print(str(len(clt)+1)+'. Regresar')
            print('Hint: Puedes escoger varias opciones a la vez, ejemplo: 1,2,4\n')
            lista=[int(i)for i in input().split(',')]
            

            query="""SELECT * FROM Clientes WHERE"""
            #datos=[]
            for i,elemento in enumerate(lista):
                if elemento==1:
                    datos.append(input('Nombre: '))
                    if i>0:
                        query += """ and Nombre = %s"""
                    else:
                        query += """ Nombre = %s"""
                    
                elif elemento==2:
                    datos.append(input('Aperllido Paterno: '))
                    if i>0:
                        query += """ and Apellido_Paterno = %s"""
                    else:
                        query += """ Apellido_Paterno = %s"""


                elif elemento==3:

                    datos.append(input('Apellido Materno: '))
                    if i>0:
                        query += """ and Apellido_Materno = %s"""
                    else:
                        query += """ Apellido_Materno = %s"""

                else:
                    break







        elif opcion_busqueda==2:
            query="""SELECT * FROM Clientes WHERE RFC = %s"""
            rfc=input('RFC: ')
            #datos=[rfc]
            datos.append(rfc)


        elif opcion_busqueda==3:

            print('Elige tus criterios de busqueda')
            for i,e in enumerate(dr):
                print(str(i+1)+'.',e)
            
            print(str(len(clt)+1)+'. Regresar')
            print('Hint: Puedes escoger varias opciones a la vez, ejemplo: 1,2,4\n')
            lista=[int(i)for i in input().split(',')]
            

            query="""SELECT * FROM Direcciones WHERE"""
            #datos=[]
            for i,elemento in enumerate(lista):
                if elemento==1:
                    datos.append(input('Calle: '))
                    if i>0:
                        query += """ and Calle = %s"""
                    else:
                        query += """ Calle = %s"""
                    
                elif elemento==2:
                    datos.append(input('Colonia: '))
                    if i>0:
                        query += """ and Colonia = %s"""
                    else:
                        query += """ Colonia = %s"""


                elif elemento==3:

                    datos.append(input('Estado: '))
                    if i>0:
                        query += """ and Estado = %s"""
                    else:
                        query += """ Estado = %s"""


                elif elemento==4:
                    datos.append(input('CP: '))
                    if i>0:
                        query += """ and CP = %s"""
                    else:
                        query += """ CP = %s"""

                else:
                    break






        elif opcion_busqueda==4:
            all_client(['Morelia','Patzcuar'],cnxs)





        if len(datos)>0:
            #print(datos)
            clientes_T=[]
            for c,cnx in enumerate(cnxs):
                cursor=cnx.cursor()
                #print(query)




                cursor.execute(query,tuple(datos))
                clientes=cursor.fetchall()
                clientes_T.append([c,clientes])
            if opcion_busqueda==3:
                for elemento in clientes_T:
                    for registro in elemento[1]:
                        print(sucursales[elemento[0]],registro)
                        nquery="SELECT * FROM Clientes WHERE Id = '%s'"%registro[-1]
                        cursor=cnxs[elemento[0]].cursor()
                        cursor.execute(nquery)
                        print(cursor.fetchall(),'\n')
                        


    except: 
        #print('Hay fallon')
        print("< OPCION INVALIDA >")
        

    
    #for cnx in cnxs:
        #print(database.description(cnx))


def create_tables(cnx):
    name=input('Nombre de la tabla(sin espacios): ')
    n=int(input('Cuantas columnas tendra la tabla? '))
    columns=[]
    typedata=[]
    print('\nEscribe los nombres de las comulmas sin usar espacios')
    for i in range(n):
        columns.append(input('Nombre de la columna '+str(i+1)+': '))
        typedata.append(input('Tipo de dato para la columna '+str(i+1)+'(VARCHAR(50), CHAR(8), etc): '))

    pk=input('Tendra llave primaria? si/no  ')
    fk=input('Tendra llave foranea? si/no  ')


   # query="""CREATE TABLE Clientes (
    #            Id                CHAR(8)      NOT NULL   PRIMARY KEY,
     #           Nombre            VARCHAR(40)  NOT NULL,
      #          Apellido_Paterno  VARCHAR(30)  NOT NULL,
       #         Apellido_Materno  VARCHAR(30)  NOT NULL,
        #        RFC               VARCHAR(13)  NOT NULL);"""

    
    pki=None
    fki=None
    fks=None

    if pk == 'si':
        for i,col in enumerate(columns):
            print(str(i+1)+'.',col)
        pki=int(input('Cual columna es llave primaria? (numero): '))

    if fk == 'si':
        for i,col in enumerate(columns):
            print(str(i+1)+'.',col)

        fki=int(input('Cual columna es llave foranea? (numero): '))
        sets=database.primary_kys(cnxs[0])
        for i,s in enumerate(sets):
            print(str(i+1)+'.',s)
        fks=int(input('Desde donde viene la llave foranea? (numero): '))

    #print(columns[pki-1],columns[fki-1],sets[fks-1])

    query="CREATE TABLE %s ("%name
    for i,elemento in enumerate(columns):
        if pki:
            if i == pki-1:
                query+="%s %s PRIMARY KEY,"%(elemento,typedata[i])
            else:
                if i == len(columns)-1:
                    query+="%s %s"%(elemento,typedata[i]) 
                else:
                    query+="%s %s,"%(elemento,typedata[i]) 
            if i == len(columns)-1:
                if not fki:
                    query+=""")"""

        else:
            #query+="""%s %s,"""
            if i==len(columns)-1:
                if not fki:
                    query+="%s %s)"%(elemento,typedata[i]) 
            else:
                query+="%s %s,"%(elemento,typedata[i]) 
    
        
    #print(sets[fks-1])

    if fki:
        query+="FOREIGN KEY (%s) REFERENCES %s (%s))"%(columns[fki-1],sets[fks-1][0],sets[fks-1][1][0])
#FOREIGN KEY (Id_Cliente) REFERENCES  Clientes (Id)
    print(query)

    #datos_to_query=[name]
    #for j,dat in enumerate(columns):
     #   datos_to_query.append(dat)
      #  datos_to_query.append(typedata[j])
    #print('echale ojo mi cans',datos_to_query)

    

    for cnx in cnxs:
        cursor=cnx.cursor()
        cursor.execute(query)
        cnx.commit()


if __name__=='__main__':
    sucursales,cnxs = database.init_databases()
    for cnx in cnxs:
        print(database.primary_kys(cnx)) 

    create_tables(cnxs)
    #buscar_clientes(sucursales,cnxs)

