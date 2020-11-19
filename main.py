import database
import processing

cnx_morelia=database.morelia()
cnx_patzcuaro=database.patzcuaro()

print(processing.prueba(cnx_morelia))
