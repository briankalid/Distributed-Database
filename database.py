import json
import mysql.connector
from mysql.connector import errorcode

def init_databases():
    
    dtbs=[]
    sucursales=[]

    with open('dbcentral.json') as json_file:
        config=json.load(json_file)
        json_file.close()

    try:
        cnxcentral = mysql.connector.connect(**config)
        print('\n'+'\033[0;32m'+'Conexion a la base de datos central exitosa'+'\033[0;m')
        cursorcentral=cnxcentral.cursor()
        
        query="""SELECT * FROM _databases_"""
        cursorcentral.execute(query)
        aux=cursorcentral.fetchall()
        
        for u,v,w,x,y in aux:
            d={}
            d['user']=v
            d['password']=w
            d['host']=x
            d['database']=y
            d['raise_on_warnings']=True
            
            dtbs.append(d)
            sucursales.append(u)


    except mysql.connector.Error as err:
            print('Base de datos central')
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)



    cnxs=[]
    for i,db in enumerate(dtbs):
        try:
            cnx = mysql.connector.connect(**db)
            print('\n'+'\033[0;32m'+'Conexion a la base de datos de',sucursales[i],'exitosa'+'\033[0;m')
            cnxs.append(cnx)

        except mysql.connector.Error as err:
                print(sucursales[i])
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)

    return sucursales,cnxs

def description(cnx):
    cursor=cnx.cursor()
    query="""SHOW TABLES"""
    cursor.execute(query)
    #cnx.commit()
    tablas=[i[0] for i in cursor.fetchall()]
    columns=[]

    for elemento in tablas:
        query="DESCRIBE %s" % elemento 
        #data_query=elemento
        #print(tuple(data_query))
        cursor.execute(query)
        columns.append(cursor.fetchall())

    return tablas,columns


