import json
import mysql.connector
from mysql.connector import errorcode






def init_databases():
    
    dtbs=[]

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
        
#{"user": "briankalid", "password": "232159", "host": "localhost", "database": "credential", "raise_on_warnings": true}
        for u,v,w,x,y in aux:
            d={}
            d['user']=v
            d['password']=w
            d['host']=x
            d['database']=y
            d['raise_on_warnings']=True
            
            dtbs.append(d)

     #   cnxs.append(cnx)
    #cursorp = cnxp.cursor()
    #return cnxp

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
        #file = 'db'+db+'.json'
        #print(file)
        #with open(file) as json_file:
        #config = json.load(db)
            #json_file.close()


        try:
            cnx = mysql.connector.connect(**db)
            print('\n'+'\033[0;32m'+'Conexion a la base de datos de',db,'exitosa'+'\033[0;m')
            cnxs.append(cnx)
            #cursorp = cnxp.cursor()
            #return cnxp

        except mysql.connector.Error as err:
                print(db)
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)

    return cnxs


