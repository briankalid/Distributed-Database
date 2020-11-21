import json
import mysql.connector
from mysql.connector import errorcode

def init_databases(dtbs):
    cnxs=[]
    for i,db in enumerate(dtbs):
        file = 'db'+db+'.json'
        print(file)
        with open(file) as json_file:
            config = json.load(json_file)
            json_file.close()


        try:
            cnx = mysql.connector.connect(**config)
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


