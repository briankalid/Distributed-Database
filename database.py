import json
import mysql.connector
from mysql.connector import errorcode

with open('dbmorelia.json') as json_file:
    configmore = json.load(json_file)
    json_file.close()

with open('dbpatzcuaro.json') as json_file:
    configpatz = json.load(json_file)
    json_file.close()



try:
    cnxm = mysql.connector.connect(**configmore)
    print('\n'+'\033[0;32m'+'Conexion a la base de datos de Morelia exitosa'+'\033[0;m')
    cursorm = cnxm.cursor()


except mysql.connector.Error as err:
        print('Morelia:')
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

try:
    cnxp = mysql.connector.connect(**configpatz)
    print('\n'+'\033[0;32m'+'Conexion a la base de datos de Patzcuaro exitosa'+'\033[0;m')
    cursorp = cnxp.cursor()


except mysql.connector.Error as err:
        print('Patzcuaro:')
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)




